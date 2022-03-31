"""Результаты анализа сохранить в виде комментариев в файле с кодом.
1. Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.

Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

Примечание по профилированию кода:
для получения достоверных результатов при замере времени необходимо
исключить/заменить функции print() и input() в анализируемом коде.
С ними вы будете замерять время вывода данных в терминал и время,
потраченное пользователем, на ввод данных,
а не быстродействие самого алгоритма.
"""
import random
import cProfile

random.seed(21)
# les1_hw_task7
"""
1.7. Определить, является ли год, который ввел пользователь,
високосным или не високосным.
"""
"""
Условия високосного года:
Если год не делится на 4, значит он обычный.
Иначе надо проверить не делится ли год на 100.
    Если не делится, значит это не столетие и можно сделать вывод,
        что год високосный.
    Если делится на 100, значит это столетие
    и его следует проверить делимость на 400.
        Если год делится на 400, то он високосный.
        Иначе год обычный.
"""


def test_leap(func):

    lst = {1888: "Високосный", 1892: "Високосный", 1896: "Високосный",
           1904: "Високосный", 1939: "Не високосный", 1964: "Високосный",
           1992: "Високосный", 2000: "Високосный", 2021: "Не високосный"}

    for key, value in lst.items():
        assert value == func(key)
        print(f'Test leap {key} OK')
    print(f'Number of test: {len(lst.keys())}')


def get_leap_year(num_y):

    if num_y % 4 == 0:
        if num_y % 100 != 0:
            return "Високосный"
        elif num_y % 400 == 0:
            return "Високосный"
        else:
            return "Не високосный"
    else:
        return "Не високосный"


# test_leap(get_leap_year)
cProfile.run('get_leap_year(1992)')

"""Запуск через консоль:
timeit

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_leap_year(1939)"
100 loops, best of 5: 205 nsec per loop

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_leap_year(19391939)"
100 loops, best of 5: 241 nsec per loop

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_leap_year(193919391939)"
100 loops, best of 5: 268 nsec per loop


O(1) - алгоритм с постоянной скоростью
Примечания:
    Закоментировать тесты функций
"""

"""
cProfile.run('get_leap_year(1939)')
4 function calls in 0.000 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:54(get_leap_year)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('get_leap_year(193998765432)')
4 function calls in 0.000 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:54(get_leap_year)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


O(1) - время выполнения всегда одно и тоже
(максимальное количесво проверок внутри функции 3)
"""

# les2_hw_task3
"""2.3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def test_revers(func):

    lst = {"1888": "8881", "1892": "2981", "1896": "6981",
           "1904": "4091", "1939": "9391", "1964": "4691",
           "1992": "2991", "2000": "0002", "2021": "1202"}

    for key, value in lst.items():
        assert value == func(key)
        print(f'Test revers {key} OK')
    print(f'Number of test: {len(lst.keys())}')


def get_revers(nums):

    new_nums = ""
    for num in nums:
        new_nums = num + new_nums
    return new_nums


# test_revers(get_revers)
# cProfile.run('get_revers("85456")')

"""Запуск через консоль:
timeit

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_revers('0123456789')"
100 loops, best of 5: 1.16 usec per loop


python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_revers('01234567890123456789')"
100 loops, best of 5: 2.12 usec per loop

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_revers('012345678901234567890123456789')"
100 loops, best of 5: 3 usec per loop

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_revers('0123456789012345678901234567890123456789')"
100 loops, best of 5: 4.34 usec per loop

O(n) - линейный алгоритм
Примечания:
    Закоментировать тесты функций
"""

"""
cProfile.run('get_revers("85456")')
4 function calls in 0.000 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:89(get_revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('get_revers("85456854568545685456854568545685456854568545685456")')
4 function calls in 0.000 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:89(get_revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""
# les2_hw_task4
"""2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""
serises_test = [1, -0.5, 0.25, -0.125, 0.0625, -0.03125, 0.015625, -0.0078125,
                0.00390625, -0.001953125, 0.0009765625, -0.00048828125,
                0.000244140625, -0.0001220703125, 6.103515625e-05,
                -3.0517578125e-05, 1.52587890625e-05, -7.62939453125e-06,
                3.814697265625e-06]
# print(sum(serises_test[:5]))


def test_sum_series(func):

    lst = {1: 1, 2: 0.5, 3: 0.75, 4: 0.625, 5: 0.6875, 6: 0.65625, 7: 0.671875,
           8: 0.6640625, 9: 0.66796875, 10: 0.666015625, 11: 0.6669921875,
           12: 0.66650390625, 13: 0.666748046875, 14: 0.6666259765625,
           15: 0.66668701171875, 16: 0.666656494140625, 17: 0.6666717529296875,
           18: 0.6666641235351562, 19: 0.6666679382324219, }

    for key, value in lst.items():
        assert value == func(key)
        print(f'Test sum series {key} OK')
    print(f'Number of test: {len(lst.keys())}')


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

    return sum_n


# test_sum_series(get_sum_series)
# cProfile.run('get_sum_series(10000)')

"""Запуск через консоль:
timeit

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_sum_series(100)"
100 loops, best of 5: 14.8 usec per loop

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_sum_series(1000)"
100 loops, best of 5: 165 usec per loop

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_sum_series(10000)"
100 loops, best of 5: 1.73 msec per loop

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_sum_series(100000)"
100 loops, best of 5: 17.3 msec per loop

python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_sum_series(1000000)"
100 loops, best of 5: 116 msec per loop


Примечания:
    Закоментировать тесты функций
"""

"""
cProfile.run('get_sum_series(10000)')
4 function calls in 0.002 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.002    0.002    0.002    0.002 les4_hw_task1.py:126(get_sum_series)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('get_sum_series(1000000)')
4 function calls in 0.121 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.121    0.121 <string>:1(<module>)
        1    0.121    0.121    0.121    0.121 les4_hw_task1.py:126(get_sum_series)
        1    0.000    0.000    0.121    0.121 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('get_sum_series(10000000)')
4 function calls in 1.165 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.165    1.165 <string>:1(<module>)
        1    1.165    1.165    1.165    1.165 les4_hw_task1.py:126(get_sum_series)
        1    0.000    0.000    1.165    1.165 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('get_sum_series(100000000)')
4 function calls in 11.876 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   11.876   11.876 <string>:1(<module>)
        1   11.876   11.876   11.876   11.876 les4_hw_task1.py:126(get_sum_series)
        1    0.000    0.000   11.876   11.876 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


O(n) - линейный алгоритм
"""

# les3_hw_task2
"""
3.2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.
"""


def test_idx_evenitm(func):

    lst = {(21, 53, 88, 53, 81, 36, 61, 27, 60, 65,): (2, 5, 8,),
           (8, 3, 15, 6, 4, 2,): (0, 3, 4, 5,),
           (2, 4, 6, 8, 9, 16, 19, 32,): (0, 1, 2, 3, 5, 7,)}

    for key, value in lst.items():
        assert list(value) == func(list(key))
        print(f'Test idx even item {list(key)} OK')
    print(f'Number of test: {len(lst.keys())}')


def get_idx_evenitm(array):
    array_2 = []
    for idx, itm in enumerate(array):
        if itm % 2 == 0:
            array_2.append(idx)

    return array_2


# test_idx_evenitm(get_idx_evenitm)
# array_cprof = [random.randint(1, 1000) for _ in range(1000000)]
# cProfile.run('get_idx_evenitm(array_cprof)')

"""Запуск через консоль:
timeit

python3 -m timeit -n 100 -s "import random" "import les4_hw_task1" "les4_hw_task1.get_idx_evenitm([random.randint(1, 1000) for _ in range(100)])"
100 loops, best of 5: 137 usec per loop

python3 -m timeit -n 100 -s "import random" "import les4_hw_task1" "les4_hw_task1.get_idx_evenitm([random.randint(1, 1000) for _ in range(1000)])"
100 loops, best of 5: 1.43 msec per loop

python3 -m timeit -n 100 -s "import random" "import les4_hw_task1" "les4_hw_task1.get_idx_evenitm([random.randint(1, 1000) for _ in range(10000)])"
100 loops, best of 5: 14.2 msec per loop

python3 -m timeit -n 100 -s "import random" "import les4_hw_task1" "les4_hw_task1.get_idx_evenitm([random.randint(1, 1000) for _ in range(100000)])"
100 loops, best of 5: 101 msec per loop


python3 -m timeit -n 100 -s "import random" "import les4_hw_task1" "les4_hw_task1.get_idx_evenitm([random.randint(1, 1000) for _ in range(1000000)])"
100 loops, best of 5: 988 msec per loop

Примечания:
    Закоментировать тесты функций
"""
"""
array_cprof = [random.randint(1, 1000) for _ in range(100)]
cProfile.run('get_idx_evenitm(array_cprof)')
48 function calls in 0.000 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:166(get_idx_evenitm)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       44    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

array_cprof = [random.randint(1, 1000) for _ in range(1000)]
cProfile.run('get_idx_evenitm(array_cprof)')
 507 function calls in 0.000 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:166(get_idx_evenitm)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      503    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

array_cprof = [random.randint(1, 1000) for _ in range(100000)]
cProfile.run('get_idx_evenitm(array_cprof)')
50025 function calls in 0.017 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.017    0.017 <string>:1(<module>)
        1    0.014    0.014    0.017    0.017 les4_hw_task1.py:166(get_idx_evenitm)
        1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
    50021    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

array_cprof = [random.randint(1, 1000) for _ in range(1000000)]
cProfile.run('get_idx_evenitm(array_cprof)')
500013 function calls in 0.170 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.170    0.170 <string>:1(<module>)
        1    0.136    0.136    0.165    0.165 les4_hw_task1.py:244(get_idx_evenitm)
        1    0.000    0.000    0.170    0.170 {built-in method builtins.exec}
   500009    0.029    0.000    0.029    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

array_cprof = [random.randint(1, 1000) for _ in range(10000000)]
cProfile.run('get_idx_evenitm(array_cprof)')
5002407 function calls in 1.781 secondss
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.047    0.047    1.781    1.781 <string>:1(<module>)
        1    1.424    1.424    1.734    1.734 les4_hw_task1.py:244(get_idx_evenitm)
        1    0.000    0.000    1.781    1.781 {built-in method builtins.exec}
  5002403    0.310    0.000    0.310    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

O(n) - линейный алгоритм
"""

# les3_hw_task9
"""3.9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Примечание: попытайтесь решить задания без использования функций
max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.
В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве
несколько раз, используйте один любой по вашему выбору.
"""
"""
input: N=2
--------------------
   22   54
   89   54
--------------------
output: (54, 2)
--------------------

input: N=4
--------------------
   22   54   89   54
   82   37   62   28
   61   66   24   65
   68   31    1    2
--------------------
output: (31, 2)
--------------------

input: N=5
--------------------
   22   54   89   54   82
   37   62   28   61   66
   24   65   68   31    1
    2   48   75   55    9
   19   97   30   30   89
-------------------------
output: (48, 2)
--------------------

input: N=10
--------------------
   22   54   89   54   82   37   62   28   61   66
   24   65   68   31    1    2   48   75   55    9
   19   97   30   30   89    6   56   95   99   53
   79   57    5   43   70   64   89   15   84   48
    3   20   95   12   16    3   59   21   71   94
   44   52   63   20   24   86    5   61   31   10
   26   27   87   85   97   98   75   94   10   16
   72   61   72   50   26   44   19   69   53   38
   47   58   65   50   41   63   50   35    4   12
   21   92   92   64    1   63    9   71   77   96
--------------------------------------------------
output: (20, 2)
--------------------
"""


def test_max_in_mincolitm(func):

    lst = {2: (54, 2), 4: (31, 2), 5: (48, 2), 10: (20, 2)}

    for key, value in lst.items():
        assert value == func(key)
        print(f'Test max in min item in columns {key} OK')
    print(f'Number of test: {len(lst.keys())}')


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

    return (itm_max, idx_max + 1)


# test_max_in_mincolitm(get_max_in_mincolitm)
# cProfile.run('get_max_in_mincolitm(10000)')


"""Запуск через консоль:
timeit
python3 -m timeit -n 100 -s "import les4_hw_task1" "les4_hw_task1.get_max_in_mincolitm(10)"

"les4_hw_task1.get_max_in_mincolitm(10)"
100 loops, best of 5: 181 usec per loop

"les4_hw_task1.get_max_in_mincolitm(100)"
100 loops, best of 5: 14.2 msec per loop

"les4_hw_task1.get_max_in_mincolitm(1000)"
100 loops, best of 5: 1.04 sec per loop


Примечания:
    Закоментировать тесты функций
"""


"""
cProfile.run('get_max_in_mincolitm(10)')
         653 function calls in 0.000 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:375(get_max_in_mincolitm)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:377(<listcomp>)
        1    0.000    0.000    0.000    0.000 random.py:123(seed)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {function Random.seed at 0x7f8795acbaf0}
      110    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      135    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('get_max_in_mincolitm(100)')
63127 function calls in 0.025 seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
        1    0.006    0.006    0.025    0.025 les4_hw_task1.py:375(get_max_in_mincolitm)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:377(<listcomp>)
        1    0.000    0.000    0.000    0.000 random.py:123(seed)
    10000    0.007    0.000    0.014    0.000 random.py:200(randrange)
    10000    0.004    0.000    0.018    0.000 random.py:244(randint)
    10000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {function Random.seed at 0x7f7965682af0}
    10100    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13019    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('get_max_in_mincolitm(1000)')
6294448 function calls in 2.229 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    2.229    2.229 <string>:1(<module>)
        1    0.541    0.541    2.227    2.227 les4_hw_task1.py:375(get_max_in_mincolitm)
        1    0.000    0.000    0.000    0.000 les4_hw_task1.py:377(<listcomp>)
        1    0.000    0.000    0.000    0.000 random.py:123(seed)
  1000000    0.635    0.000    1.281    0.000 random.py:200(randrange)
  1000000    0.310    0.000    1.591    0.000 random.py:244(randint)
  1000000    0.440    0.000    0.646    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    2.229    2.229 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {function Random.seed at 0x7fa9539e5af0}
  1001000    0.094    0.000    0.094    0.000 {method 'append' of 'list' objects}
  1000000    0.090    0.000    0.090    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1293440    0.116    0.000    0.116    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('get_max_in_mincolitm(10000)')
629299182 function calls in 225.388 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.251    0.251  225.388  225.388 <string>:1(<module>)
        1   54.354   54.354  225.136  225.136 les4_hw_task1.py:375(get_max_in_mincolitm)
        1    0.002    0.002    0.002    0.002 les4_hw_task1.py:377(<listcomp>)
        1    0.000    0.000    0.000    0.000 random.py:123(seed)
100000000   64.653    0.000  129.525    0.000 random.py:200(randrange)
100000000   32.893    0.000  162.418    0.000 random.py:244(randint)
100000000   44.859    0.000   64.872    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000  225.388  225.388 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {function Random.seed at 0x7f82938d6af0}
100010000    8.362    0.000    8.362    0.000 {method 'append' of 'list' objects}
100000000    8.825    0.000    8.825    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
129289174   11.189    0.000   11.189    0.000 {method 'getrandbits' of '_random.Random' objects}

O(n**2)
"""

