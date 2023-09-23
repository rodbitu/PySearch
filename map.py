import math

def calculate_distance_points(map, start, goal):
    # Desempacota as coordenadas dos pontos
    x1, y1 = start
    x2, y2 = goal

    # Verifica se as coordenadas dos pontos estão dentro da matriz (limites de 1 a 10)
    limits = (1 <= x1 < 11) and (1 <= y1 < 11) and (1 <= x2 < 11) and (1 <= y2 < 11)
    if not limits:
        raise ValueError("Coordenadas dos pontos estão fora da matriz")

    # Calcula a distância euclidiana entre os pontos
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

    # distance = calcular_distancia_pontos(mapa, ponto1, ponto2)
    # print(f"A distância entre {ponto1} e {ponto2} na matriz é: {distancia:.2f}")



# def borda(filaDeEstados, listafechada):
#     filaDeEstados

#     return


def initialize_map(lines = 11, columns = 11, standard_value = 0):
    return [[standard_value] * columns for _ in range(lines)]


def print_map(map):
    # Mapeamento de valores de célula para caracteres
    cell_symbols = {
        0: "⬛",     # Cubo disponível
        100: "⬜",   # Cubo indisponível
        200: "🏁",  # Objetivo
        300: "⧈",   # Cubo visitado
        400: "🟦",  # Inicio
    }

    # Imprimir o mapa
    for line in map:
        for cell in line:
            # Usar get() para obter o valor padrão se não estiver no dicionário
            symbol = cell_symbols.get(cell, str(cell))
            print(" ", symbol, end=" ")
        print()  # Nova linha para a próxima linha do mapa



# Pontos para calcular a distância
goal = (2, 5) # Objetivo
start = (10, 5) # Inicio

# Inicializar o mapa transformando em uma matriz
map = initialize_map()

# Espaço indisponível
map[0][0] = "⬜"

# Adicionar números de 1 a 10 na primeira coluna
for i in range(1, 11):
    map[i][0] = i

# Adicionar letras de A a J na primeira linha
letters = "ABCDEFGHIJ"
for i, letter in enumerate(letters):
    map[0][i + 1] = letter

# Adicionar cubos indisponiveis (100)
black_cubes = [(1, 6), (2, 6), (3, 6), (3, 5), (3, 4), (3, 3), (4, 3), (5, 3), (6, 3), (5, 5), (6, 5), (7, 5), (8, 5), (8, 4), (9, 4), (10, 4)]
for x, y in black_cubes:
    map[x][y] = 100

# Adicionar cubo de objetivo (200)
line_goal, column_goal = goal
map[line_goal][column_goal] = 200

# Adicionar cubo de inicio (400)
line_start, column_start = start
map[line_start][column_start] = 400


print_map(map)
