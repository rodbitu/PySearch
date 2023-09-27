def initialize_map(lines=11, columns=11, standard_value=0):
    return [[standard_value] * columns for _ in range(lines)]


def print_map(map):
    # Mapeamento de valores de célula para caracteres
    cell_symbols = {
        0: "🔲",  # Cubo disponível
        1000: "🔳",  # Cubo indisponível
        2000: "🏁",  # Objetivo
        3000: "🟥",  # Explorado mas não percorridos
        4000: "🟩",  # Cubo visitado
        5000: "🟦",  # Inicio
    }

    # Imprimir o mapa
    for line in map:
        for cell in line:
            # Usar get() para obter o valor padrão se não estiver no dicionário
            symbol = cell_symbols.get(cell, str(cell))
            print(" ", symbol, end=" ")
        print()  # Nova linha para a próxima linha do mapa


# Inicializar o mapa transformando em uma matriz
map = initialize_map()

map[0][0] = "🔳"

numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
# Adicionar números de 1 a 10 na primeira coluna
for i, number in enumerate(numbers):
    map[i + 1][0] = number

# Adicionar letras de A a J na primeira linha
for i, number in enumerate(numbers):
    map[0][i + 1] = number

# Adicionar cubos indisponiveis (1000)
black_cubes = [
    (1, 6),
    (2, 6),
    (3, 6),
    (3, 5),
    (3, 4),
    (3, 3),
    (4, 3),
    (5, 3),
    (6, 3),
    (5, 5),
    (6, 5),
    (7, 5),
    (8, 5),
    (8, 4),
    (9, 4),
    (10, 4),
]
for x, y in black_cubes:
    map[x][y] = 1000

# Adicionar cubo de objetivo (2000)
goal = input("Qual a coordenada do objetivo? Ex:(linha, coluna)")
goal = eval(goal) if goal else (2, 5)
line_goal, column_goal = goal
map[line_goal][column_goal] = 2000

# Adicionar cubo de inicio (5000)
start = input("Qual a coordenada do inicio? Ex:(linha, coluna)")
start = eval(start) if start else (10, 5)
line_start, column_start = start
map[line_start][column_start] = 5000


print_map(map)
