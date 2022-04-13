"""
3. Массив размером 2m + 1, где m — натуральное число,
заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
    в одной находятся элементы, которые не меньше медианы,
    в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
from random import randint

m = randint(3, 10)
size = 2 * m + 1
array = [randint(1, 100) for i in range(size)]
array0 = array.copy()
array1 = array.copy()


def get_median(array):
    """Функция поиска медианны на основе того что:
    Медианой называется элемент ряда, делящий его на 'ДВЕ РАВНЫЕ ЧАСТИ':
        в одной находятся элементы, которые 'НЕ МЕНЬШЕ' медианы,
        в другой — 'НЕ БОЛЬШЕ' медианы."""
    for itm in array:
        not_less = 0    # 'НЕ МЕНЬШЕ'
        not_more = 0    # 'НЕ БОЛЬШЕ'

        for _itm in array:
            if itm > _itm:
                # подсчет элементов 'НЕ БОЛЬШЕ' числа (itm) верхнего цикла
                not_more += 1
            elif itm < _itm:
                # подсчет элементов 'НЕ МЕНЬШЕ' числа (itm) верхнего цикла
                not_less += 1

        if not_less == not_more:
            return itm


def gnome_sort(array):
    """гномья сортировка списка array"""
    i = 1
    while i < len(array):
        if i == 0 or array[i - 1] <= array[i]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array


def digit_rank_sort(array):
    """поразрядная сортировка списка array"""
    base = 10
    digit_len = len(str(max(array)))
    for i in range(digit_len):
        result = [[] for _ in range(base)]
        for rank in array:
            di_rank = rank // 10**i % 10
            result[di_rank].append(rank)
        array = []
        for j in range(base):
            array = array + result[j]
    return array


print(f'Исходный список:\n{array}\n'
      f'Медиана с помощью функции {get_median.__name__}: {get_median(array)}\n'
      f'Список отсортированный функцией {gnome_sort.__name__}:\n'
      f'{gnome_sort(array0)}\nмедианна по гномей сортировке:\n'
      f'{gnome_sort(array0)[len(array)//2]}\n'
      f'Список отсортированный функцией {digit_rank_sort.__name__}:\n'
      f'{digit_rank_sort(array1)}\nмедианна по поразрядной сортировке:\n'
      f'{digit_rank_sort(array1)[len(array)//2]}')


def test_sort(sort_algorithm):
    print(f'Тестируем: {sort_algorithm.__name__}\n{sort_algorithm.__doc__}')

    print("testcase #1: ", end="")
    array = [22, 54, 89, 54, 82, 37, 62, 28, 61, 66, 24]
    array_sorted = [22, 24, 28, 37, 54, 54, 61, 62, 66, 82, 89]

    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")

    print("testcase #2: ", end="")
    array = list(range(1, 20)) + list(range(20, 40))
    array_sorted = list(range(1, 40))

    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")

    print("testcase #3: ", end="")
    array = [82, 15, 4, 95, 36, 32, 29, 18, 95, 14, 87]
    array_sorted = [4, 14, 15, 18, 29, 32, 36, 82, 87, 95, 95]

    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")
    print('*' * 21)


def test_median(median_func):
    print(f'Тестируем: {median_func.__name__}\n{median_func.__doc__}')
    print("testcase #1: ", end="")
    array = [-100, -60, -20, -40, -80, 79, 99, 59, 19, 39, 100]
    mediann = sorted(array)[len(array)//2]

    print("Ok" if median_func(array) == mediann else "Fail")
    print('*' * 21)


if __name__ == "__main__":
    test_sort(gnome_sort)
    test_sort(digit_rank_sort)
    test_median(get_median)
