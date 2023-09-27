from map import map, print_map, goal, start
from operations import validate_points
import math
import time

map
goal
start
queueOfStates = []  # Explorados
closedList = []  # Percorrido
edge = []  # Não percorrido mas explorado

validate_points(start, goal)


def calculate_euclidiana_distance(start, goal):
    # Desempacota as coordenadas dos pontos
    x1, y1 = start
    x2, y2 = goal

    # Calcula a distância euclidiana
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_manhattan_distance(start, goal):
    # Desempacota as coordenadas dos pontos
    x1, y1 = start
    x2, y2 = goal

    # Calcula a distância de Manhattan
    return abs(x2 - x1) + abs(y2 - y1)


def sucessores(start, goal, map):
    descobertaAtual = []

    # Calculo da borda
    for data in queueOfStates:
        if data not in closedList:
            edge.append(data)

    l, c = start

    def is_valid_position(x, y):
        return 0 <= x < len(map) and 0 <= y < len(map[0])

    for dl in range(-1, 2):
        for dc in range(-1, 2):
            if dl == 0 and dc == 0:
                continue  # Ignorar a própria posição

            new_l, new_c = l + dl, c + dc

            if is_valid_position(new_l, new_c):
                if map[new_l][new_c] == 0 or (new_l, new_c) in edge:
                    map[new_l][new_c] = 3000
                    if (new_l, new_c) not in queueOfStates:
                        queueOfStates.append((new_l, new_c))

                    if (new_l, new_c) not in closedList:
                        descobertaAtual.append((new_l, new_c))

                if map[new_l][new_c] == 2000:
                    print_map(map)
                    print("Objetivo encontrado!")
                    return

    time.sleep(2)
    print_map(map)
    print()
    buscaHeuristica(descobertaAtual, map, goal)


# Busca heurística gulosa
def buscaHeuristica(descobertaAtual, map, goal):
    distancias = []

    print("Descoberta atual: ", descobertaAtual)
    if len(descobertaAtual) > 0:
        for pos in descobertaAtual:
            print(math.floor(calculate_manhattan_distance(pos, goal)))
            distancias.append(math.floor(calculate_manhattan_distance(pos, goal)))

        iDoMenorDist = distancias.index(min(distancias))
        posMenorDist = descobertaAtual[iDoMenorDist]

        print("Menor distância: ", posMenorDist)
        closedList.append(posMenorDist)

        sucessores(posMenorDist, goal, map)
