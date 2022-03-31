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


def fib_loop(n):
    if n < 2:
        return n

    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second

    return second


# test_fib(fib_loop)
# cProfile.run('fib_list(500)')


""" cProfile

cProfile.run('fib_dict(10)')
23 function calls (5 primitive calls) in 0.000 seconds
19/1    0.000    0.000    0.000    0.000 task_5.py:26(_fib_list)


cProfile.run('fib_dict(20)')
43 function calls (5 primitive calls) in 0.000 seconds
39/1    0.000    0.000    0.000    0.000 task_5.py:26(_fib_list)


cProfile.run('fib_dict(100)')
203 function calls (5 primitive calls) in 0.000 seconds
199/1    0.000    0.000    0.000    0.000 task_5.py:26(_fib_list)

cProfile.run('fib_dict(500)')
1003 function calls (5 primitive calls) in 0.001 seconds
999/1    0.001    0.000    0.001    0.001 task_5.py:26(_fib_list)
"""

"""timeit in terminal
python3 -m timeit -n 1000 -s "import task_6" "task_6.fib_loop(10)"

"task_6.fib_loop(10)"
1000 loops, best of 5: 719 nsec per loop

"task_6.fib_loop(15)"
1000 loops, best of 5: 1.02 usec per loop

"task_6.fib_loop(20)"
1000 loops, best of 5: 1.14 usec per loop

"task_6.fib_loop(100)"
1000 loops, best of 5: 4.99 usec per loop

"task_6.fib_loop(200)"
1000 loops, best of 5: 10.1 usec per loop

"task_6.fib_loop(500)"
1000 loops, best of 5: 32.6 usec per loop

"task_6.fib_loop(1000)"
1000 loops, best of 5: 77 usec per loop

"task_6.fib_loop(50000)"
1000 loops, best of 5: 27.7 msec per loop
"""
