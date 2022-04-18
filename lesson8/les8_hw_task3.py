"""
3. Написать программу, которая обходит
не взвешенный ориентированный граф без петель,
в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции,
    которая принимает на вход число вершин.
"""
# from collections import deque
from random import randint, choices


def get_graph(n_vertex):
    # списки смежности в виде словаря #2 в рассмотреной лекции
    # граф в котором все вершины связаны
    graph = {str(i): None for i in range(n_vertex)}
    for j in range(n_vertex):
        # будем записывать числа в строковом формате
        j = str(j)
        # создаем множество за исключением выбраного ключа(без петель)
        g_set = set(graph.keys()) - set([j])
        # создаем множество ребер с помощбю функции random.choices
        # со случайным количеством елементов от 2 до число_вершин-1
        adj_list = set(choices(list(g_set),
                               k=randint(2, n_vertex-1)))
        # преобразовываем мноество в список
        graph[j] = list(adj_list)
    return graph


def dfs(graph, v_start, visited=[]):
    # при вызове добавляем  в список пройденых вершин
    # вершину переданную в v_start
    visited.append(v_start)

    for v in graph[v_start]:
        # если не посещали вершину
        if v not in visited:
            # вызываем рекурсивно функцию
            # передавая в нее выбраную вершину v_start = v
            # и список пройденыхвершин visited
            dfs(graph, v, visited)

    return visited


n_vertex = int(input('Введите количество вершин: '))
v_start = input("Введите вершину начала: ")

graph = get_graph(n_vertex)
print('Списки смежности сгенерированного графа:',
      '-' * 50,
      *graph.items(),
      sep='\n')
print(f'{"*" * 50}\nОбход графа по алгоритму Depth-First Search (dfs):\n\t'
      f'{dfs(graph, v_start)}')
