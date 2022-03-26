"""8. Матрица 5x4 заполняется вводом с клавиатуры,
кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []
for line in range(5):
    matrix.append([])
    sum_line = 0

    for i in range(3):
        item = int(input(f'Введите число строк[{line}] столбец[{i}]: '))
        matrix[line].append(item)
        sum_line += item
    matrix[line].append(sum_line)

for line in matrix:
    for i, item in enumerate(line):

        print(f"{item:>5}", end='')
    print()
print('-' * (len(matrix) * 5))
