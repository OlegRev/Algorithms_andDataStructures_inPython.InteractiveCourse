import sys

sys.setrecursionlimit(3000)


def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))


def akk_1(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk_1(m - 1, 1)
    elif m > 0 and n > 0:
        return akk_1(m - 1, akk_1(m, n - 1))
    return 'Что то не так'


m, n = 2, 8
print(f"{akk(m, n)}\n{'**' * 3}\n{akk_1(m, n)}")
