"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Примечание: попытайтесь решить задания без использования функций
max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.

В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве
несколько раз, используйте один любой по вашему выбору.
"""
import random

N = 4   # Для матрицы 4х4

min_col = [float('inf') for _ in range(N)]

matrix = []
for idx_line in range(N):
    matrix.append([])
    for idx in range(N):
        item = random.randint(1, 10)
        if item < min_col[idx]:
            min_col[idx] = item
        matrix[idx_line].append(item)


for line in matrix:
    for i, item in enumerate(line):

        print(f"{item:>5}", end='')
    print()
print('-' * (len(matrix) * 5))
print('Минимальные числа столбцов:\n')


itm_max = float('-inf')
for idx, itm in enumerate(min_col):
    print(f"{itm:>5}", end='')
    if itm > itm_max:
        itm_max = itm
        idx_max = idx

print(f'\nМаксимальный элемент среди минимальных элементов столбцов матрицы:\n'
      f'\tчисло:{itm_max:>17}\n\tнаходиться в столбце: {idx_max + 1}')
