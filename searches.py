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
cost = 0 # Custo do caminho

validate_points(start, goal)


def calculate_euclidiana_distance(start, goal):
    # Desempacota as coordenadas dos pontos
    x1, y1 = start
    x2, y2 = goal

    # Calcula a distância euclidiana
    value = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return {"value": value, "name": "euclidiana_distance"}


def calculate_manhattan_distance(start, goal):
    # Desempacota as coordenadas dos pontos
    x1, y1 = start
    x2, y2 = goal

    # Calcula a distância de Manhattan
    value = abs(x2 - x1) + abs(y2 - y1)
    return {"value": value, "name": "manhattan_distance"}


def exploration(start, goal, map, distance):
    currentDiscovery = []
    explored = []

    # Calculo da borda
    for data in queueOfStates:
        if data not in closedList:
            edge.append(data)

    l, c = start

    def is_valid_position(x, y):
        return 0 <= x < len(map) and 0 <= y < len(map[0])

    for dl in range(-1, 2):
        for dc in range(-1, 2):
            if distance(start, goal)["name"] == "euclidiana_distance":
                if dl == 0 and dc == 0:
                    continue  # Ignorar a própria posição

            new_l, new_c = l + dl, c + dc
            explored.append((new_l, new_c))

    if distance(start, goal)["name"] == "manhattan_distance":
        explored = [value for indice, value in enumerate(explored) if indice % 2 != 0]

    for pos in explored:
        new_l, new_c = pos
        if is_valid_position(new_l, new_c):
            if map[new_l][new_c] == 0 or (new_l, new_c) in edge:
                if (new_l, new_c) not in queueOfStates:
                    map[new_l][new_c] = 3000
                    queueOfStates.append((new_l, new_c))

                if (new_l, new_c) not in closedList:
                    map[new_l][new_c] = 3000
                    currentDiscovery.append((new_l, new_c))

            if map[new_l][new_c] == 2000:
                print_map(map)
                print("Custo: ", cost)
                print("Objetivo encontrado!")
                return True

    time.sleep(2)
    print_map(map)
    print()
    heuristicSearch(currentDiscovery, map, goal, distance)


# Busca heurística gulosa
def heuristicSearch(currentDiscovery, map, goal, distance):
    distancias = []

    if currentDiscovery == []:
        print("Objetivo não encontrado!")
        return False

    print("Descoberta atual: ", currentDiscovery)
    if len(currentDiscovery) > 0:
        for pos in currentDiscovery:
            distancias.append(math.floor(distance(pos, goal)["value"]))

        iDoMenorDist = distancias.index(min(distancias))
        posMenorDist = currentDiscovery[iDoMenorDist]
        
        global cost
        cost  += min(distancias)

        print("Menor distância: ", posMenorDist)
        closedList.append(posMenorDist)
        x, y = posMenorDist
        map[x][y] = 4000

        exploration(posMenorDist, goal, map, distance)      
    


# Inicializa a busca heurística gulosa com a distância euclidiana
exploration(start, goal, map, calculate_euclidiana_distance)

# Initializa a busca heurística gulosa com a distância de Manhattan
exploration(start, goal, map, calculate_manhattan_distance)
