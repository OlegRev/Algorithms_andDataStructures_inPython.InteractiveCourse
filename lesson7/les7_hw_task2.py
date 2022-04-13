"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform


size = 11
start = 0
stop = 49

array0 = [uniform(start, stop) for i in range(size)]
array1 = array0.copy()


def merge_array(left, right):
    """Функция слияния двух отсортированных списков"""
    merge = []
    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1

    merge += left[i:] + right[j:]

    return merge


def splitmerge_array(array):
    """Функция деления списка на два списка до len(списка) == 1
    Затем вызов функции слияния двух отсортированных списков
    Вариант с двумя функциями"""
    mid = len(array)//2
    left, right = array[:mid], array[mid:]

    if len(left) > 1:
        left = splitmerge_array(left)
    if len(right) > 1:
        right = splitmerge_array(right)

    return merge_array(left, right)


def merge_sort(array):
    """Сортировка списка array методом слияния
    Вариант с одной функцией"""
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


print(f'Исходный список:\n{array0}\n')
array0 = splitmerge_array(array0)
print(f'Сортированный список функцией {splitmerge_array.__name__}:\n'
      f'{array0}\n')
print('*' * 50)
print(f'Исходный список:\n{array1}\n')
array1 = merge_sort(array1)
print(f'Сортированный список функцией {merge_sort.__name__}:\n{array1}\n')


def test_sort(sort_algorithm):
    """Функция тестирования сортировок
    """
    print(f'Тестируем: {sort_algorithm.__name__}\n{sort_algorithm.__doc__}')

    print("testcase #1: ", end="")
    array = [-100.1, -60.2, -20.3, -40.4, -80.5,
             79.6, 99.7, 59.8, 19.9, 39.11]
    array_sorted = [-100.1, -80.5, -60.2, -40.4, -20.3,
                    19.9, 39.11, 59.8, 79.6, 99.7]

    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")

    print("testcase #2: ", end="")
    array = list(range(0, 20)) + list(range(-19, 0))
    array_sorted = list(range(-19, 20, 1))

    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")

    print("testcase #3: ", end="")
    array = [-100.123, -80.124, -20.24, -100.123, -80.124,
             79.4567, 99.3456, 99.3456, 19.456, 39.2354]
    array_sorted = [-100.123, -100.123, -80.124, -80.124, -20.24,
                    19.456, 39.2354, 79.4567, 99.3456, 99.3456]

    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")

    print("testcase #4: ", end="")
    array = [uniform(0, 49) for i in range(10)]
    array_sorted = sorted(array)

    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")
    print('*' * 21)


if __name__ == "__main__":
    test_sort(merge_sort)
    test_sort(splitmerge_array)
