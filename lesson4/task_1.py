import timeit

x = 2 + 2
print(timeit.timeit('x = 2 + 2'))
print(timeit.timeit('x = sum(range(10))'))

"""Запуск через консоль:
python3 -m timeit -n 100 -s "import task_1"
"""
