import random
import sys

"""1. Подсчитать, сколько было выделено памяти под переменные
в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.

Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным
решением будет:
    a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;

    b. написать 3 варианта кода (один у вас уже есть);
    проанализировать 3 варианта и выбрать оптимальный;

    c. результаты анализа (количество занятой памяти в вашей среде разработки)
    вставить в виде комментариев в файл с кодом.
    Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

    d. написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof
после каждой переменной, а проявили творчество, фантазию и создали
универсальный код для замера памяти."""


def show_size(x, level=0):
    """Функция с урока"""
    print('\t' * level, f'type= {x.__class__}, '
          f'size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


def show_sum_size(x, level=0):
    """Добавим в функцию написаную на уроке сумирование по объектам
    и удалим лишние выводы на экран
    """
    res_size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for k, v in x.items():
                res_size += show_sum_size(k, level + 1)
                res_size += show_sum_size(v, level + 1)

        elif not isinstance(x, str):
            for v in x:
                res_size += show_sum_size(v, level + 1)

    return res_size


def get_sum_memory(func, func_arg):
    print('-*-' * 21)
    result_sum_mem = 0
    res_variables = []
    for key, value in func(func_arg).items():
        # print(f'\n\nПеременная {key}:\n{"=" * 20}')
        if key == 'N' or key == 'n':
            N = value
        result_sum_mem += show_sum_size(value)
        res_variables.append((key, value.__class__, show_sum_size(value)))

    print(f'Переменные функции {func.__name__}({N})'
          f' занимают\n{result_sum_mem} байт памяти')
    for itm in res_variables:
        print(itm)
    print('-*-' * 21)


"""3.9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Примечание: попытайтесь решить задания без использования функций
max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.
В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве
несколько раз, используйте один любой по вашему выбору.
"""


def get_max_in_mincolitm(N):
    random.seed(21)
    min_col = [float('inf') for _ in range(N)]
    matrix = []
    for idx_line in range(N):
        matrix.append([])
        for idx in range(N):
            item = random.randint(1, 99)
            if item < min_col[idx]:
                min_col[idx] = item
            matrix[idx_line].append(item)

    itm_max = float('-inf')
    for idx, itm in enumerate(min_col):
        if itm > itm_max:
            itm_max = itm
            idx_max = idx
    # return (itm_max, idx_max + 1)
    return locals()    # выводим словарь всез локальных переменных функции


"""2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def get_sum_series(n):
    """элементов ряда 1, -0.5, 0.25, -0.125, ..., n
    a(i), a(i+1)= a(i)/(-2), a(i+2) = a(i+1)/(-2)... : """
    a = 1
    enum = 0
    sum_n = 0

    while enum != n:
        sum_n += a
        a = a/(-2)
        enum += 1

    # return sum_n
    return locals()


"""2.3. Сформировать из введенного числа
обратное по порядку входящих в него цифр
и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def get_revers(N):
    random.seed(21)
    N = str(random.randint(9999, 999999))
    new_nums = ""
    for num in N:
        new_nums = num + new_nums
    # return new_nums
    return locals()


def get_revers1(N):
    random.seed(21)
    N = str(random.randint(9999, 999999))
    N = reversed(N)
    # return new_nums
    return locals()


def get_revers2(N):
    random.seed(21)
    N = str(random.randint(9999, 999999))
    N = N[::-1]
    # return new_nums
    return locals()


print(f'Версия python: {sys.version}\nПлатформа: {sys.platform}\n')
func_list = [get_max_in_mincolitm,
             get_sum_series,
             get_revers,
             get_revers1,
             get_revers2]
for function in func_list:
    get_sum_memory(function, func_arg=10)


"""
Версия python: 3.8.13 (default, Mar 26 2022, 22:17:55) [GCC]
Платформа: linux

-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-
Переменные функции get_max_in_mincolitm(10) занимают
5484 байт памяти
('N', <class 'int'>, 28)
('min_col', <class 'list'>, 464)
('matrix', <class 'list'>, 4824)
('idx_line', <class 'int'>, 28)
('idx', <class 'int'>, 28)
('item', <class 'int'>, 28)
('itm_max', <class 'int'>, 28)
('itm', <class 'int'>, 28)
('idx_max', <class 'int'>, 28)
-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-
-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-
Переменные функции get_sum_series(10) занимают
104 байт памяти
('n', <class 'int'>, 28)
('a', <class 'float'>, 24)
('enum', <class 'int'>, 28)
('sum_n', <class 'float'>, 24)
-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-
-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-
Переменные функции get_revers(182961) занимают
160 байт памяти
('N', <class 'str'>, 55)
('new_nums', <class 'str'>, 55)
('num', <class 'str'>, 50)
-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-
-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-
Переменные функции get_revers1(<reversed object at 0x7f8d66c421f0>) занимают
348 байт памяти
('N', <class 'reversed'>, 48)
-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-
-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-
Переменные функции get_revers2(169281) занимают
55 байт памяти
('N', <class 'str'>, 55)
-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-


get_revers2
Занимает меньше всего памяти из трех функций реверса введенной цифры
get_revers1
Использует встроенную функцию и имеет меньшую память переменной
но общую память занимает больше засчет использования
объекта-функции(предположительно)

Другие реализации функций можно было придумать на основе словарей и кортеже
и посмотреть что лучше но это уже разработка в обратную сторону как по мне.
"""
