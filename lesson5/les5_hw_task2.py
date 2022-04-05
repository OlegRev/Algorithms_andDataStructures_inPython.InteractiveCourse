"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого — цифры числа.

Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями hex() и/или int()
для преобразования систем счисления, задача решается в несколько строк.
Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы
счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""

from collections import deque


def digit_hex(d):
    """
    Замена литерал в данной очереди на значения в 10-ой системе счисления
    """
    for idx, item in enumerate(d):
        if item == 'A':
            d[idx] = 10
        elif item == 'B':
            d[idx] = 11
        elif item == 'C':
            d[idx] = 12
        elif item == 'D':
            d[idx] = 13
        elif item == 'E':
            d[idx] = 14
        elif item == 'F':
            d[idx] = 15


def hex_dec(d, a):
    """
    Преобразование из 16-ричной системы счисления
    в 10-ичную для очереди и получении суммы по всем элементам
    """
    for i in range(len(d)):
        a.append(int(d[i])*16**i)
    return sum([i for i in a])


def dec_hex(d):
    """
    Преобразование числа в 10-ой системе счисления
    в число 16-ричной системы счисления
    """
    alphabet = "0123456789ABCDEF"
    n = int(d)
    if n < 16:
        return alphabet[n]
    else:
        return dec_hex(n // 16) + alphabet[n % 16]


digital_1 = deque(input('введите первое число: ').upper())
digital_2 = deque(input('введите второе число: ').upper())
sumbol = input('введите символ операции над числами ("+" "*" "-" "/")\n'
               'для операций "-" и "/" вычесляется абсалютное значение: ')
res1 = deque()
res2 = deque()

if len(digital_1) > len(digital_2):
    digital_2.appendleft(0)
elif len(digital_1) < len(digital_2):
    digital_1.appendleft(0)

digit_hex(digital_1)
digit_hex(digital_2)
digital_1.reverse()
digital_2.reverse()

hex_dec(digital_1, res1)
hex_dec(digital_2, res2)

if sumbol == '+':
    print(dec_hex(sum([i for i in res1]) + sum([i for i in res2])))
elif sumbol == '*':
    print(dec_hex(sum([i for i in res1]) * sum([i for i in res2])))
elif sumbol == '-':
    print(dec_hex(abs(sum([i for i in res1]) - sum([i for i in res2]))))
elif sumbol == '/':
    print(dec_hex(abs(sum([i for i in res1]) / sum([i for i in res2]))))


