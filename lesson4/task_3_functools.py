import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


cProfile.run('fib(200)')

# test_fib(fib)

"""cProfile.run('fib(10)')
14 function calls (4 primitive calls) in 0.000 seconds
11/1    0.000    0.000    0.000    0.000 task_3_functools.py:11(fib)


cProfile.run('fib(100)')
104 function calls (4 primitive calls) in 0.000 seconds
101/1    0.000    0.000    0.000    0.000 task_3_functools.py:11(fib)


cProfile.run('fib(200)')
204 function calls (4 primitive calls) in 0.000 seconds
201/1    0.000    0.000    0.000    0.000 task_3_functools.py:11(fib)

"""

"""Запуск через консоль:
timeit
python3 -m timeit -n 1000 -s "import task_3_functools" "task_3_functools.fib(10)"

"task_3_functools.fib(10)"
1000 loops, best of 5: 101 nsec per loop

"task_3_functools.fib(100)"
1000 loops, best of 5: 147 nsec per loop

"task_3_functools.fib(200)"
1000 loops, best of 5: 97.2 nsec per loop

"""
