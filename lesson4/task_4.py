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


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


# test_fib(fib_dict)
cProfile.run('fib_dict(500)')
""" cProfile
cProfile.run('fib_dict(10)')
23 function calls (5 primitive calls) in 0.000 seconds
19/1    0.000    0.000    0.000    0.000 task_4.py:25(_fib_dict)

cProfile.run('fib_dict(20)')
43 function calls (5 primitive calls) in 0.000 seconds
39/1    0.000    0.000    0.000    0.000 task_4.py:25(_fib_dict)

cProfile.run('fib_dict(100)')
203 function calls (5 primitive calls) in 0.000 seconds
199/1    0.000    0.000    0.000    0.000 task_4.py:25(_fib_dict)

cProfile.run('fib_dict(500)')
1003 function calls (5 primitive calls) in 0.001 seconds
999/1    0.001    0.000    0.001    0.001 task_4.py:25(_fib_dict)
"""

"""timeit in terminal
python3 -m timeit -n 1000 -s "import task_4" "task_4.fib_dict(10)"

"task_4.fib_dict(10)"
1000 loops, best of 5: 5.13 usec per loop

"task_4.fib_dict(15)"
1000 loops, best of 5: 7.6 usec per loop

"task_4.fib_dict(20)"
1000 loops, best of 5: 10.6 usec per loop

"task_4.fib_dict(100)"
1000 loops, best of 5: 53.8 usec per loop

"task_4.fib_dict(200)"
1000 loops, best of 5: 108 usec per loop

"task_4.fib_dict(500)"
1000 loops, best of 5: 333 usec per loop

"task_4.fib_dict(1000)"
    fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
  [Previous line repeated 988 more times]
RecursionError: maximum recursion depth exceeded


"""
