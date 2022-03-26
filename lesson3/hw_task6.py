"""6. В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве
несколько раз, используйте один любой по вашему выбору.
"""
import random

array = [random.randint(0, 10) for _ in range(10)]
# максимальное и минимальное число (hw_task3)
itm_max = float('-inf')
itm_min = float('inf')
for idx, itm in enumerate(array):
    if itm > itm_max:
        itm_max = itm
        idx_max = idx
    if itm < itm_min:
        itm_min = itm
        idx_min = idx

summ_itms = 0
if idx_max > idx_min:
    for itm in array[idx_min+1:idx_max]:
        summ_itms += itm
elif idx_max < idx_min:
    for itm in array[idx_max+1:idx_min]:
        summ_itms += itm

print(f"Массив array:\t{array}\n"
      f"Максимальное число array[{idx_max}]:\t{itm_max}\n"
      f"Минимальное число array[{idx_min}]:\t{itm_min}\n"
      f"{'-' * 33}\n"
      f"Сумма чисел между\nмаксимальным и минимальным\nчислами равно:"
      f"\t\t\t{summ_itms}")

