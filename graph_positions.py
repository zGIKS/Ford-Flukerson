def get_predefined_positions(n):
    positions = {
        8: {
            0: (0, 1),   # Izquierda
            1: (1, 2),   # Arriba izquierda
            2: (1, 0),   # Abajo izquierda
            3: (2, 0),   # Centro izquierda
            4: (2, 2),   # Centro abajo
            5: (3, 2),   # Arriba derecha
            6: (3, 0),   # Centro derecha
            7: (4, 1)  # Abajo derecha
        },
        9: {
            0: (0, 1),   # Izquierda
            1: (1, 2),   # Arriba izquierda
            2: (1, 0),   # Abajo izquierda
            3: (2, 0),   # Centro izquierda
            4: (2, 2),   # Centro abajo
            5: (3, 1),   # Arriba derecha
            6: (4, 0),   # Centro derecha
            7: (4, 2),  # Abajo derecha
            8: (5, 1)    
        },
        10: {
            0: (0, 1),   # Izquierda
            1: (1, 2),   # Arriba izquierda
            2: (1, 0),   # Abajo izquierda
            3: (2, 0),   # Centro izquierda
            4: (2, 2),   # Centro abajo
            5: (3, 2),   # Arriba derecha
            6: (3, 0),   # Centro derecha
            7: (4, 0),  # Abajo derecha
            8: (4, 2),   
            9: (5, 1)   
        },
        11: {
            0: (0, 1),   # Izquierda
            1: (1, 2),   # Arriba izquierda
            2: (1, 0),   # Abajo izquierda
            3: (2, 0),   # Centro izquierda
            4: (2, 2),   # Centro abajo
            5: (3, 1),   # Arriba derecha
            6: (4, 0),   # Centro derecha
            7: (4, 2),  # Abajo derecha
            8: (5, 0) ,   
            9: (5, 2),  
            10: (6, 1)   
        },
        12: {
            0: (0, 1),   # Izquierda
            1: (1, 2),   # Arriba izquierda
            2: (1, 0),   # Abajo izquierda
            3: (2, 0),   # Centro izquierda
            4: (2, 2),   # Centro abajo
            5: (3, 2),   # Arriba derecha
            6: (3, 0),   # Centro derecha
            7: (4, 0),  # Abajo derecha
            8: (4, 2),   
            9: (5, 0),  
            10: (5, 2),  
            11: (6, 1)  
        },
        13: {
            0: (0, 1),   # Izquierda
            1: (1, 2),   # Arriba izquierda
            2: (1, 0),   # Abajo izquierda
            3: (2, 0),   # Centro izquierda
            4: (2, 2),   # Centro abajo
            5: (3, 1),   # Arriba derecha
            6: (4, 0),   # Centro derecha
            7: (4, 2),  # Abajo derecha
            8: (5, 0) ,   
            9: (5, 2),  
            10: (6, 0),  
            11: (6, 2), 
            12: (7, 1)   
        },
        14: {
            0: (0, 1),   # Izquierda
            1: (1, 2),   # Arriba izquierda
            2: (1, 0),   # Abajo izquierda
            3: (2, 0),   # Centro izquierda
            4: (2, 2),   # Centro abajo
            5: (3, 2),   # Arriba derecha
            6: (3, 0),   # Centro derecha
            7: (4, 0),  # Abajo derecha
            8: (4, 2),   
            9: (5, 0),  
            10: (5, 2),  
            11: (6, 0), 
            12: (6, 2),  
            13: (7, 1)   
        },
        15: {
            0: (0, 1),   # Izquierda
            1: (1, 2),   # Arriba izquierda
            2: (1, 0),   # Abajo izquierda
            3: (2, 0),   # Centro izquierda
            4: (2, 2),   # Centro abajo
            5: (3, 1),   # Arriba derecha
            6: (4, 0),   # Centro derecha
            7: (4, 2),  # Abajo derecha
            8: (5, 0) ,   
            9: (5, 2),  
            10: (6, 0),  
            11: (6, 2), 
            12: (7, 0),  
            13: (7, 2),  
            14: (8, 1)  
        },
        16: {
            0: (0, 1),   # Izquierda
            1: (1, 2),   # Arriba izquierda
            2: (1, 0),   # Abajo izquierda
            3: (2, 0),   # Centro izquierda
            4: (2, 2),   # Centro abajo
            5: (3, 2),   # Arriba derecha
            6: (3, 0),   # Centro derecha
            7: (4, 0),  # Abajo derecha
            8: (4, 2),   
            9: (5, 0),  
            10: (5, 2),  
            11: (6, 0), 
            12: (6, 2),  
            13: (7, 0),
            14: (7, 2),
            15: (8, 1)
        },
    }

    return positions.get(n, None)