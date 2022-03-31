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


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


# test_fib(fib_list)
cProfile.run('fib_list(500)')

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
python3 -m timeit -n 1000 -s "import task_5" "task_5.fib_list(10)"

"task_5.fib_list(10)"
1000 loops, best of 5: 9.04 usec per loop

"task_5.fib_list(15)"
1000 loops, best of 5: 11.8 usec per loop

"task_5.fib_list(20)"
1000 loops, best of 5: 14.4 usec per loop

"task_5.fib_list(100)"
1000 loops, best of 5: 56.1 usec per loop

"task_5.fib_list(200)"
1000 loops, best of 5: 111 usec per loop

"task_5.fib_list(500)"
1000 loops, best of 5: 311 usec per loop
"""
