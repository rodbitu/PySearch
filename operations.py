def validate_points(start, goal):
    # Desempacota as coordenadas dos pontos
    x1, y1 = start
    x2, y2 = goal

    # Verifica se as coordenadas dos pontos estão dentro da matriz (limites de 1 a 10)
    limits = (1 <= x1 < 11) and (1 <= y1 < 11) and (1 <= x2 < 11) and (1 <= y2 < 11)
    if not limits:
        raise ValueError("Coordenadas inacessiveis")
