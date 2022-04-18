# Матрицы смежности
# для связанных графов
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
]

print(*graph, sep='\n')
# для связанных направленных графов
print('*' * 50)
graph = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
]

print(*graph, sep='\n')
# для связанных направленных взвешенных графов
print('*' * 50)
graph[0][1:3] = [2, 3]
graph[1][2] = 2
graph[2][1] = 2

print(*graph, sep='\n')
