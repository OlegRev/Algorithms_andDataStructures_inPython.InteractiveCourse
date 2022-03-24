import random

# Вставка элемента в произвольое место массива
print('# Вставка элемента в произвольое место массива', end=f'\n{"-"*50}\n')

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Введите целое число для вставки: '))
pos = int(input('На какую позицию вставить число: '))

array.append(None)
i = len(array) - 1

while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1

array[pos] = num
print(array, end=f'\n{"-"*50}\n')

# с использованием встроенного метода insert
print('\n# с использованием встроенного метода insert', end=f'\n{"-"*50}\n')

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Введите целое число для вставки: '))
pos = int(input('На какую позицию вставить число: '))

array.insert(pos, num)

array[pos] = num
print(array, end=f'\n{"-"*50}\n')

# с созданием нового списка
print('\n# с созданием нового списка', end=f'\n{"-"*50}\n')

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Введите целое число для вставки: '))
pos = int(input('На какую позицию вставить число: '))

array_new = array[:pos] + [num] + array[:pos]

array[pos] = num
print(array, end=f'\n{"-"*50}\n')
