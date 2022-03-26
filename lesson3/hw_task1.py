"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Примечание: 8 разных ответов.
"""


def get_multiples(array: list, value: int = 2) -> list:
    '''Функция получения из списка array чисел кратных value by default = 2.

    Parameters
    ----------
    array: list
        Список в котором происходит поиск кратных чисел
    value: int: 2 optional

    Returns
    -------
    res: list
        Числа из спика 'array' кратных числу 'value'

    '''
    res = [itm for itm in array if itm % value == 0]
    return res


array = [_ for _ in range(2, 100)]
values = [_ for _ in range(2, 10)]

for val in values:
    val_multiples = get_multiples(array=array, value=val)
    print(f"Для {val} кратных чисел в списке от 2 до 99 :\t"
          f"{len(val_multiples)}\n{'-' * 50}\n"
          f"{val_multiples}\n{'-' * 50}\n")

"""
Алгоритм проходит 8 раз по списку из 98 чисел,
Кажется что эффективнее было бы завести 8 списков для каждого числа,
пройтись по списку в 98 чисел один раз и произвести 8 проверок на кратность

проверка скорости выполнения в файле:
    hw_task1_timeit.py
"""

multi2, multi3, multi4, multi5 = [], [], [], []
multi6, multi7, multi8, multi9 = [], [], [], []
for itm in array:
    if itm % 2 == 0:
        multi2.append(itm)
    if itm % 3 == 0:
        multi3.append(itm)
    if itm % 4 == 0:
        multi4.append(itm)
    if itm % 5 == 0:
        multi5.append(itm)
    if itm % 6 == 0:
        multi6.append(itm)
    if itm % 7 == 0:
        multi7.append(itm)
    if itm % 8 == 0:
        multi8.append(itm)
    if itm % 9 == 0:
        multi9.append(itm)

print(f"Для {2} кратных чисел в списке от 2 до 99 :\t"
      f"{len(multi2)}\n{'-' * 50}\n{multi2}\n{'-' * 50}\n"
      f"Для {3} кратных чисел в списке от 2 до 99 :\t"
      f"{len(multi3)}\n{'-' * 50}\n{multi3}\n{'-' * 50}\n"
      f"Для {4} кратных чисел в списке от 2 до 99 :\t"
      f"{len(multi4)}\n{'-' * 50}\n{multi4}\n{'-' * 50}\n"
      f"Для {5} кратных чисел в списке от 2 до 99 :\t"
      f"{len(multi5)}\n{'-' * 50}\n{multi5}\n{'-' * 50}\n"
      f"Для {6} кратных чисел в списке от 2 до 99 :\t"
      f"{len(multi6)}\n{'-' * 50}\n{multi6}\n{'-' * 50}\n"
      f"Для {7} кратных чисел в списке от 2 до 99 :\t"
      f"{len(multi7)}\n{'-' * 50}\n{multi7}\n{'-' * 50}\n"
      f"Для {8} кратных чисел в списке от 2 до 99 :\t"
      f"{len(multi8)}\n{'-' * 50}\n{multi8}\n{'-' * 50}\n"
      f"Для {9} кратных чисел в списке от 2 до 99 :\t"
      f"{len(multi9)}\n{'-' * 50}\n{multi9}\n{'-' * 50}\n")
