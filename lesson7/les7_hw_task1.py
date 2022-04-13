"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.

Примечания:
a. алгоритм сортировки должен быть в виде функции,
    которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните,
    что у вас должна остаться сортировка пузырьком.

Улучшенные версии сортировки, например:
    расчёской, шейкерная и другие в зачёт не идут.
"""
from random import randint

size = 10
start = -100
stop = 99

array0 = [randint(start, stop) for _ in range(size)]
array1 = array0.copy()


def bubble_sort0(array):
    """Код с урока
    добавлено все в функцию и изменён знак условия
    """
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        # print(array)
    return array, n


print(array0)
print(bubble_sort0(array0))
print('*' * 50)


def bubble_sort(array):
    """Cортировка списка array методом пузырька
    с флагом перестоновок 'shift'
    """
    n = 1   # счетчик проходом по списку
    shift = True
    while shift:
        shift = False
        # флаг устанавливается в False
        # для выхода из цикла если небыло перестановок
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                shift = True    # если была перестановка то продолжение цикла
        n += 1
        # print(array)
    return array, n


print(array1)
print(bubble_sort(array1))
print('*' * 50)
# Функция тестирования сортировок


def test_sort(sort_algorithm):
    print(f'Тестируем: {sort_algorithm.__name__}\n{sort_algorithm.__doc__}')

    print("testcase #1: ", end="")
    array = [-100, -60, -20, -40, -80, 79, 99, 59, 19, 39]
    array_sorted = [99, 79, 59, 39, 19, -20, -40, -60, -80, -100]

    print("Ok" if sort_algorithm(array)[0] == array_sorted else "Fail")

    print("testcase #2: ", end="")
    array = list(range(0, 20)) + list(range(-19, 0))
    array_sorted = list(range(19, -20, -1))

    print("Ok" if sort_algorithm(array)[0] == array_sorted else "Fail")

    print("testcase #3: ", end="")
    array = [-100, -80, -20, -100, -80, 79, 99, 99, 19, 39]
    array_sorted = [99, 99, 79, 39, 19, -20, -80, -80, -100, -100]

    print("Ok" if sort_algorithm(array)[0] == array_sorted else "Fail")
    print('*' * 21)


if __name__ == "__main__":
    test_sort(bubble_sort0)
    test_sort(bubble_sort)
