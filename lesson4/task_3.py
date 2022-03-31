import cProfile


def test_fib(func):
    '''Тест для функции фибоначи

    Parameters
    ----------
    func:callable(object)
        Функция которая выдает последовательность чисел Фибоначи

    Returns
    -------
    print(Test {i} OK)
    '''
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib(n):
    '''Функция выдающая ряд чисел фибоначи до 'n'-ого элемента

    Parameters
    ----------
    n: int
        Число элемента до которого нужно вывести ряд чисел фибоначи
    Returns
    -------
    n or fib(n - 1) + fib(n - 2)
    '''
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)



cProfile.run('fib(25)')


# test_fib(fib)

"""cProfile.run('fib(10)')
180 function calls (4 primitive calls) in 0.000 seconds
177/1    0.000    0.000    0.000    0.000 task_3.py:22(fib)


cProfile.run('fib(15)')
1976 function calls (4 primitive calls) in 0.001 seconds
1973/1    0.001    0.000    0.001    0.001 task_3.py:22(fib)

cProfile.run('fib(20)')
21894 function calls (4 primitive calls) in 0.009 seconds
21891/1    0.009    0.000    0.009    0.009 task_3.py:22(fib)

cProfile.run('fib(25)')
242788 function calls (4 primitive calls) in 0.087 seconds
242785/1    0.087    0.000    0.087    0.087 task_3.py:22(fib)

"""

"""Запуск через консоль:
timeit

python3 -m timeit -n 1000 -s "import task_3" "task_3.fib(10)"

Примечания:
    Закоментировать функции которые не тестируются( test_fib())
"""

# "task_3.fib(10)"
# 1000 loops, best of 5: 26.7 usec per loop


# "task_3.fib(15)"
# 1000 loops, best of 5: 297 usec per loop

# "task_3.fib(20)"
# 1000 loops, best of 5: 2.27 msec per loop

# "task_3.fib(25)"
# 1000 loops, best of 5: 25.2 msec per loop

# Результат профилирования:
#     Cложность алгоритма ~ O(2**(n))
