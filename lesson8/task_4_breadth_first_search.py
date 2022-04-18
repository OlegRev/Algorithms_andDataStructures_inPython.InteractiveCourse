from collections import deque


g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]


def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:

        curent = deq.pop()

        if curent == finish:
            # return parent
            """
            От какой вершины идти: 2
            До какой вершины идти: 5
            [2, 0, None, None, 2, 6, 4, 6]
            """
            break

        for i, vertex in enumerate(graph[curent]):
            if vertex == 1 and not is_visited[i]:

                is_visited[i] = True
                parent[i] = curent
                deq.appendleft(i)

    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'
    # для отображения читаемого пути по графу
    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'кратчайший путь {list(way)} длинною в {cost} условных едениц'


s = int(input('От какой вершины идти: '))
f = int(input('До какой вершины идти: '))
print(bfs(g, s, f))
