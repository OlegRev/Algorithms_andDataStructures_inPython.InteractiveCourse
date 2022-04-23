"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша:
        hash(),
        sha1(),
        любой другой из модуля hashlib
    задача считается не решённой.
"""
import random


def my_index(value):
    """функция с лекции"""
    letter = 26
    index = 0
    size = 10000

    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i

    return index % size


def my_hash(value, size=10**6):
    """простая хеш функция
    """
    letter = 26
    _hash = 0

    for i, char in enumerate(value):
        random.seed(ord(char))
        some_int = (ord(char) << random.randint(ord(char) - ord('a'),
                                                ord(char)))//ord(char)
        _hash += (some_int) * letter ** i

    return _hash % size


def get_n_subs_list(string, n_subs=True):
    lenght = len(string)
    _subs = []
    # (lenght - 1) для исключения входа в список подстрок, целой строки
    for i in range(lenght - 1):
        for j in range(lenght - i):
            # print(f'i: {i}, j: {j}')
            # print(f'{string}[{j} : {j+i+1}]')
            # print(string[j:j+i+1])
            # вводим переменную для удобного опирирования условиями в цикле
            h_s = my_hash(string[j:j+i+1])
            # добавления срез от j до j+i+1 если его нет в списке подстрок
            if h_s not in _subs:
                # print(h_s, string[j:j+i+1])
                _subs.append(h_s)
    if n_subs:
        return len(_subs)
    else:
        return _subs, len(_subs)


string = input('Ввелите строку для поиска подстрок: ')

print(get_n_subs_list(string))
