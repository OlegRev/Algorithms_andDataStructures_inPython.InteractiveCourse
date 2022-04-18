"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""
from collections import deque


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    # print(f'cost: {cost}\nparent: {parent}\nis_visited: {is_visited}\n\n')
    # список очередей прохода по графу
    # можно было и без очередей,
    # в конце надо было бы развернуть список в цикле while для вывода на экран
    vertex_lists = [deque([]) for _ in range(length)]
    for i in range(length):
        # если стоимость хода меньше бесконечности и существует(!= 0)
        if cost[i] < float('inf') and cost[i]:
            # добавление в i-ую очередь_пройденых_вершин, вершину i
            vertex_lists[i].append(i)
            # приравниваем индексы вершин j и i
            j = i
            # пока у вершины j есть родитель(!=-1)
            while parent[j] != -1:
                # добавляем слева в очередь_пройденых_вершин родителя вершины j
                vertex_lists[i].appendleft(parent[j])
                # меняем индекс j на его родителя
                j = parent[j]
        # иначе приравниваем очередь к None
        else:
            vertex_lists[i] = None

    return cost, vertex_lists


s = int(input('От какой вершины идти: '))
cost, vertex_lists = dijkstra(g, s)

for idx, itm in enumerate(vertex_lists):
    print(f'Для вершины: {idx}\nСтоимость обхода: {cost[idx]}\n'
          f'Очередь обхода: {itm}\n')
