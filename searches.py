from map import map, print_map, goal, start, calculate_distance_points
import math
import time
import heapq

map
goal
start
filaDeEstados = []  # locais já explorados
listafechada = []  # caminho percorrido
borda = []  # já explorados mas não pecorrido

calculate_distance_points(map, start, goal)

# def sucessores(start, goal, map):
#     # esta função exploras os pontos ao redor
#     descobertaAtual = []

#     if start[0] - 1 > 0:
#         l = start[0] - 1
#         c = start[1]
#         for i in range(-1, 2):
#             if c + i > 0 or c + i < 11:
#                 if map[l][c + i] == 0:
#                     map[l][c + i] = 300
#                     filaDeEstados.append((l, c + i))
#                     descobertaAtual.append((l, c + i))

#                 if map[l][c + i] == 200:
#                     print_map(map)
#                     return

#     l = start[0]
#     c = start[1]
#     for i in range(-1, 2):
#         if c + i > 0 or c + i < 11:
#             if i != 0 and map[l][c + i] == 0:
#                 map[l][c + i] = 300
#                 filaDeEstados.append((l, c + i))
#                 descobertaAtual.append((l, c + i))

#             if map[l][c + i] == 200:
#                 print_map(map)
#                 return

#     if start[0] + 1 < 11:
#         l = start[0] + 1
#         c = start[1]
#         for i in range(-1, 2):
#             if c + i > 0 or c + i < 11:
#                 if map[l][c + i] == 0:
#                     map[l][c + i] = 300
#                     filaDeEstados.append((l, c + i))
#                     descobertaAtual.append((l, c + i))

#                 if map[l][c + i] == 200:
#                     print_map(map)
#                     return

#     print_map(map)
#     buscaHeuristica(descobertaAtual, map, goal)


# def buscaHeuristica(descobertaAtual, map, goal):
    # buscaHeuristica: Esta função verifica qual posição tem a menor distancia reta ate o obj
    # e chama a função susessores para explorar apartid desse ponto

    # colocar a carinha na prisão atual

    # distancias = []
    # print(descobertaAtual)
    # if descobertaAtual != []:
    #     for i in range(len(descobertaAtual)):
    #         distancias.append(
    #             math.floor(
    #                 calculate_distance_points(map, descobertaAtual[i], goal)
    #             )
    #         )

    #     for i in range(len(distancias)):
    #         if distancias[i] == min(distancias):
    #             iDoMenorDist = i
    #             print(descobertaAtual[iDoMenorDist])
    #             listafechada.append(descobertaAtual[iDoMenorDist])
    #             print("avança")
    #             time.sleep(5)
    #             sucessores(descobertaAtual[iDoMenorDist], goal, map)

    # if descobertaAtual == []:
    #     print("voltando")




import heapq

# Função para calcular a distância euclidiana entre dois pontos em uma matriz
def euclidean_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Função para calcular a distância de Manhattan entre dois pontos em uma matriz
def manhattan_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x1 - x2) + abs(y1 - y2)

# Função para encontrar o caminho A* em uma matriz 11x11
def a_star_search(map, start, goal, distance):
    rows, cols = len(map), len(map[0])
    open_list = []
    closed_set = set()
    came_from = {}

    g_score = {node: float('inf') for node in map}
    g_score[start] = 0

    f_score = {node: float('inf') for node in map}
    f_score[start] = distance(start, goal)

    heapq.heappush(open_list, (f_score[start], start))

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)
            return path

        closed_set.add(current)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current
            neighbor = (x + dx, y + dy)

            if neighbor in closed_set or neighbor[0] < 0 or neighbor[0] >= rows or neighbor[1] < 0 or neighbor[1] >= cols:
                continue

            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + distance(neighbor, goal)
                if neighbor not in open_list:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None

# Função para encontrar o caminho com busca cega uniforme em uma matriz 11x11
def uniform_cost_search(matrix, start, goal):
    rows, cols = len(matrix), len(matrix[0])
    open_list = []
    closed_set = set()
    came_from = {}

    cost = {node: float('inf') for node in matrix}
    cost[start] = 0

    heapq.heappush(open_list, (cost[start], start))

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)
            return path

        closed_set.add(current)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current
            neighbor = (x + dx, y + dy)

            if neighbor in closed_set or neighbor[0] < 0 or neighbor[0] >= rows or neighbor[1] < 0 or neighbor[1] >= cols:
                continue

            new_cost = cost[current] + 1

            if new_cost < cost[neighbor]:
                came_from[neighbor] = current
                cost[neighbor] = new_cost
                heapq.heappush(open_list, (cost[neighbor], neighbor))

    return None


a_star_search(map, start, goal, euclidean_distance)
a_star_search(map, start, goal, manhattan_distance)