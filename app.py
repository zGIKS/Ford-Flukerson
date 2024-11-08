from flask import Flask, render_template, request
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
from collections import deque
from graph_positions import get_predefined_positions  # Importar las posiciones predefinidas

app = Flask(__name__)

def generate_random_matrix(n):
    # Inicializa la matriz con ceros
    matrix = np.zeros((n, n), dtype=int)

    # Reemplazar los '1' siguiendo el patrón específico
    for i in range(n):
        for j in range(i + 1, min(n, i + 4)):  # Solo permite hasta 3 conexiones hacia adelante
            matrix[i][j] = np.random.randint(1, 10)  # Reemplaza '1' con un valor aleatorio

    return matrix

def create_graph_from_matrix(matrix):
    G = nx.DiGraph()
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] > 0:
                G.add_edge(i, j, capacity=matrix[i][j])
    return G

def bfs(G, source, sink, parent):
    visited = {node: False for node in G.nodes()}
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v in G[u]:
            if not visited[v] and G[u][v]['capacity'] - G[u][v].get('flow', 0) > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(G, source, sink):
    for u in G:
        for v in G[u]:
            G[u][v]['flow'] = 0

    parent = {}
    max_flow = 0
    flow_paths = []  # Para almacenar los caminos del flujo máximo

    while bfs(G, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        current_path = []

        while s != source:
            path_flow = min(path_flow, G[parent[s]][s]['capacity'] - G[parent[s]][s]['flow'])
            current_path.append((parent[s], s))  # Agrega el borde al camino
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            G[u][v]['flow'] += path_flow
            if G.has_edge(v, u):
                G[v][u]['flow'] -= path_flow
            else:
                G.add_edge(v, u, flow=-path_flow, capacity=0)
            v = parent[v]

        max_flow += path_flow
        flow_paths.append(current_path)  # Agrega el camino actual al flujo máximo

    return max_flow, flow_paths

def plot_graph_flow(G, n):
    pos = get_predefined_positions(n)
    if not pos:
        pos = nx.spring_layout(G)  # Si no hay posiciones predefinidas, usar un layout por defecto

    # Obtiene las capacidades de los bordes, omitiendo aquellos con capacidad 0
    weights = {(u, v): d['capacity'] for u, v, d in G.edges(data=True) if d['capacity'] > 0}

    plt.figure(figsize=(10, 8))
    
    # Dibuja el grafo con flechas unidireccionales y sin curvas
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black', font_weight='bold')
    nx.draw_networkx_edges(G, pos, edgelist=weights.keys(), arrowstyle='-|>', arrowsize=15, connectionstyle='arc3')  # Flechas rectas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_size=8, label_pos=0.3)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def plot_max_flow_graph(G, flow_paths, n):
    pos = get_predefined_positions(n)
    if not pos:
        pos = nx.spring_layout(G)  # Si no hay posiciones predefinidas, usar un layout por defecto

    plt.figure(figsize=(10, 8))

    # Dibuja los nodos
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black', font_weight='bold')

    # Dibuja todas las aristas en negro
    all_edges = list(G.edges())
    nx.draw_networkx_edges(G, pos, edgelist=all_edges, edge_color='black', arrows=True)

    # Resalta las aristas del flujo máximo en rojo
    max_flow_edges = [edge for path in flow_paths for edge in path]
    nx.draw_networkx_edges(G, pos, edgelist=max_flow_edges, edge_color='red', arrows=True, arrowstyle='-|>', arrowsize=20)

    # Obtiene los flujos de cada arista
    flow_labels = {(u, v): f"{G[u][v]['flow']}/{G[u][v]['capacity']}" for u, v in max_flow_edges}
    
    # Dibuja las etiquetas de flujo en las aristas del flujo máximo
    nx.draw_networkx_edge_labels(G, pos, edge_labels=flow_labels, font_color='red', font_size=8, label_pos=0.3)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return base64.b64encode(buf.getvalue()).decode('utf-8')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_matrix', methods=['POST'])
def select_matrix():
    n = int(request.form['matrix_size'])

    if request.form['matrix_type'] == 'random':
        matrix = generate_random_matrix(n)
        return render_template('matrix_input.html', matrix=matrix, n=n, random=True)
    else:
        return render_template('matrix_input.html', matrix=None, n=n, random=False)


@app.route('/generate_graph', methods=['POST'])
def generate_graph():
    n = int(request.form['n'])
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            value = int(float(request.form[f'matrix_{i}_{j}']))
            row.append(value)
        matrix.append(row)

    matrix = np.array(matrix, dtype=int)

    # Verificar si la matriz está compuesta solo por ceros
    if np.all(matrix == 0):
        return render_template('error.html', error_message="Syntax Error: La matriz no puede contener solo ceros.")

    G = create_graph_from_matrix(matrix)
    max_flow_value, flow_paths = ford_fulkerson(G, 0, n-1)

    # Dibuja el grafo original
    graph_img = plot_graph_flow(G, n)

    # Dibuja el grafo resaltando el flujo máximo
    max_flow_graph_img = plot_max_flow_graph(G, flow_paths, n)

    matrix_str = np.array2string(matrix)
    return render_template(
        'graph.html', 
        graph_img=graph_img, 
        max_flow_graph_img=max_flow_graph_img, 
        matrix_str=matrix_str, 
        max_flow=max_flow_value, 
        n=n
    )


@app.route('/calculate_new_flow', methods=['POST'])
def calculate_new_flow():
    n = int(request.form['n'])
    source = int(request.form['source'])
    sink = int(request.form['sink'])

    # Crea la matriz a partir de los datos enviados en el formulario
    matrix = []
    for i in range(n):
        # Elimina los corchetes y espacios adicionales
        row = request.form[f'matrix_{i}'].replace('[', '').replace(']', '').split()
        matrix.append(list(map(int, row)))

    matrix = np.array(matrix)
    G = create_graph_from_matrix(matrix)

    # Calcula el flujo máximo entre los nuevos vértices seleccionados
    max_flow_value, flow_paths = ford_fulkerson(G, source, sink)

    # Dibuja el grafo original nuevamente
    graph_img = plot_graph_flow(G, n)

    # Dibuja el grafo con el nuevo flujo máximo resaltado
    max_flow_graph_img = plot_max_flow_graph(G, flow_paths, n)

    matrix_str = np.array2string(matrix)
    return render_template(
        'graph.html', 
        graph_img=graph_img,  # Mantiene la imagen del grafo original
        max_flow_graph_img=max_flow_graph_img, 
        matrix_str=matrix_str, 
        max_flow=max_flow_value, 
        n=n
    )


if __name__ == '__main__':
    plt.switch_backend('Agg')
    app.run(debug=True)
