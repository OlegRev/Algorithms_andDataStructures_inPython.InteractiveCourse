"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

>>> sieve(2)
3
>>> prime(4)
7
>>> sieve(5)
11
>>> prime(1)
2

Примечание по профилированию кода:
для получения достоверных результатов при замере времени необходимо
исключить/заменить функции print() и input() в анализируемом коде.
С ними вы будете замерять время вывода данных в терминал и время,
потраченное пользователем, на ввод данных,
а не быстродействие самого алгоритма.
"""

import cProfile

# Реалзация алгоритма Решето Эратосфена на Python lesson2 task7.py
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def sieve_eratosthenes(num):
    if num < 1:
        return False
    result = [2, 3]    # ввод первых двух чисел для решета
    n = num    # ввод числа "n" для формирования решета(код из лекции 2 task7.py)
    # если длина списка решета меньше введенного числа то умножить
    while len(result) < num:
        n *= 2
        sieve = [i for i in range(n)]
        sieve[1] = 0
        for i in range(2, n):
            if sieve[i] != 0:
                j = i * 2
                while j < n:
                    sieve[j] = 0
                    j += i
        result = [i for i in sieve if i != 0]
        # print(result)
    return result[num - 1]


# cProfile.run('sieve_eratosthenes(1000000)')


"""cProfile.run('sieve_eratosthenes(10)')
11 function calls in 0.000 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les4_hw_task2.py:37(sieve_eratosthenes)
        2    0.000    0.000    0.000    0.000 les4_hw_task2.py:44(<listcomp>)
        2    0.000    0.000    0.000    0.000 les4_hw_task2.py:52(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve_eratosthenes(1000)')
14 function calls in 0.007 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.006    0.006    0.007    0.007 les4_hw_task2.py:37(sieve_eratosthenes)
        3    0.001    0.000    0.001    0.000 les4_hw_task2.py:44(<listcomp>)
        3    0.000    0.000    0.000    0.000 les4_hw_task2.py:52(<listcomp>)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('sieve_eratosthenes(100000)')
17 function calls in 2.282 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.025    0.025    2.282    2.282 <string>:1(<module>)
        1    1.948    1.948    2.257    2.257 les4_hw_task2.py:37(sieve_eratosthenes)
        4    0.178    0.045    0.178    0.045 les4_hw_task2.py:44(<listcomp>)
        4    0.130    0.033    0.130    0.033 les4_hw_task2.py:52(<listcomp>)
        1    0.000    0.000    2.282    2.282 {built-in method builtins.exec}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('sieve_eratosthenes(1000000)')
17 function calls in 23.935 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.203    0.203   23.935   23.935 <string>:1(<module>)
        1   21.142   21.142   23.731   23.731 les4_hw_task2.py:37(sieve_eratosthenes)
        4    1.547    0.387    1.547    0.387 les4_hw_task2.py:44(<listcomp>)
        4    1.042    0.261    1.042    0.261 les4_hw_task2.py:52(<listcomp>)
        1    0.000    0.000   23.935   23.935 {built-in method builtins.exec}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

"""
python3 -m timeit -n 100 -s "import les4_hw_task2" "les4_hw_task2.sieve_eratosthenes(10)"
"les4_hw_task2.sieve_eratosthenes(10)"
100 loops, best of 5: 19.3 usec per loop

"les4_hw_task2.sieve_eratosthenes(100)"
100 loops, best of 5: 539 usec per loop

"les4_hw_task2.sieve_eratosthenes(1000)"
100 loops, best of 5: 6.77 msec per loop

"les4_hw_task2.sieve_eratosthenes(10000)"
100 loops, best of 5: 122 msec per loop

"""


"""Перебор делителей — алгоритм тестирования простоты числа
путем полного перебора всех возможных потенциальных делителей.

Перебор делителей заключается в переборе всех целых (как вариант: простых)
чисел от 2 до квадратного корня из тестируемого числа n и в вычислении
остатка от деления n на каждое из этих чисел.
Если остаток от деления на некоторое число m равен нулю,
то m является делителем n — в этом случае n объявляется составным,
и алгоритм заканчивает работу.
При достижении квадратного корня из n и невозможности сократить n ни на одно
из меньших чисел, n объявляется простым.
"""


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def get_prime_num(n):
    prime_n = 2
    no_prime = 1
    num_check = 3
    while no_prime < n:
        if is_prime(num_check):
            prime_n = num_check
            no_prime += 1
        num_check += 2
    return prime_n


# cProfile.run('get_prime_num(1000000)')


"""cProfile.run('get_prime_num(10)')
18 function calls in 0.000 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       14    0.000    0.000    0.000    0.000 les4_hw_task2.py:140(is_prime)
        1    0.000    0.000    0.000    0.000 les4_hw_task2.py:149(get_prime_num)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('get_prime_num(1000)')
3963 function calls in 0.011 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
     3959    0.009    0.000    0.009    0.000 les4_hw_task2.py:140(is_prime)
        1    0.002    0.002    0.011    0.011 les4_hw_task2.py:149(get_prime_num)
        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('get_prime_num(100000)')
649858 function calls in 11.102 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   11.102   11.102 <string>:1(<module>)
   649854   10.820    0.000   10.820    0.000 les4_hw_task2.py:140(is_prime)
        1    0.282    0.282   11.102   11.102 les4_hw_task2.py:149(get_prime_num)
        1    0.000    0.000   11.102   11.102 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('get_prime_num(1000000)')
7742935 function calls in 280.202 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  280.202  280.202 <string>:1(<module>)
  7742931  277.729    0.000  277.729    0.000 les4_hw_task2.py:140(is_prime)
        1    2.474    2.474  280.202  280.202 les4_hw_task2.py:149(get_prime_num)
        1    0.000    0.000  280.202  280.202 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


"""
python3 -m timeit -n 100 -s "import les4_hw_task2" "les4_hw_task2.get_prime_num(10)"
100 loops, best of 5: 8.89 usec per loop

"les4_hw_task2.get_prime_num(100)"
100 loops, best of 5: 289 usec per loop

"les4_hw_task2.get_prime_num(1000)"
100 loops, best of 5: 8.98 msec per loop

"les4_hw_task2.get_prime_num(10000)"
100 loops, best of 5: 188 msec per loop

"""
