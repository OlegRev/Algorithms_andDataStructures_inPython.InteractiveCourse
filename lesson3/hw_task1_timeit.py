import timeit

test_cod1 = """
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
val_all = []    # добавлено на втором прогоне
for val in values:
    val_multiples = get_multiples(array=array, value=val)
    val_all.append(val_multiples)    # добавлено на втором прогоне

"""
test_cod2 = """
array = [_ for _ in range(2, 100)]
values = [_ for _ in range(2, 10)]
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


"""
el_number = 100000

elapsed_time2 = timeit.timeit(test_cod2, number=el_number)/el_number
elapsed_time1 = timeit.timeit(test_cod1, number=el_number)/el_number
print(f"Время выполнения варианта 1: {elapsed_time1}\n"
      f"Время выполнения варианта 2: {elapsed_time2}\n")

elapsed_time1 = timeit.timeit(test_cod1, number=el_number)/el_number
elapsed_time2 = timeit.timeit(test_cod2, number=el_number)/el_number
print(f"Время выполнения варианта 1: {elapsed_time1}\n"
      f"Время выполнения варианта 2: {elapsed_time2}\n")

elapsed_time2 = timeit.timeit(test_cod2, number=el_number)/el_number
elapsed_time1 = timeit.timeit(test_cod1, number=el_number)/el_number
print(f"Время выполнения варианта 1: {elapsed_time1}\n"
      f"Время выполнения варианта 2: {elapsed_time2}\n")

elapsed_time1 = timeit.timeit(test_cod1, number=el_number)/el_number
elapsed_time2 = timeit.timeit(test_cod2, number=el_number)/el_number
print(f"Время выполнения варианта 1: {elapsed_time1}\n"
      f"Время выполнения варианта 2: {elapsed_time2}\n")

"""Проверка показала что эффективность первого варианта
лучше второго проверка.

el_number = 100000:

Время выполнения варианта 1: 5.583134966000216e-05
Время выполнения варианта 2: 6.026891547999185e-05

Время выполнения варианта 1: 3.9176665080012756e-05
Время выполнения варианта 2: 4.099980003999008e-05

Время выполнения варианта 1: 3.898054272000081e-05
Время выполнения варианта 2: 4.103434890999779e-05

Время выполнения варианта 1: 3.9758933949997297e-05
Время выполнения варианта 2: 4.1067338649991145e-05

Второй прогон:
    добавление общего списка и добавление списка кратных в общий список

Время выполнения варианта 1: 5.6014053319995584e-05
Время выполнения варианта 2: 5.87339731999964e-05

Время выполнения варианта 1: 3.967914732000281e-05
Время выполнения варианта 2: 4.0154817580005326e-05

Время выполнения варианта 1: 3.91370341000038e-05
Время выполнения варианта 2: 4.0313431340000534e-05

Время выполнения варианта 1: 3.910811478001051e-05
Время выполнения варианта 2: 4.018271860000823e-05


"""
