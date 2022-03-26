"""3. В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.

В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве
несколько раз, используйте один любой по вашему выбору.
"""
import random

array = [random.randint(0, 100) for _ in range(10)]
array_new = array[:]
itm_max = float('-inf')
itm_min = float('inf')
for idx, itm in enumerate(array):
    if itm > itm_max:
        itm_max = itm
        idx_max = idx
    if itm < itm_min:
        itm_min = itm
        idx_min = idx

array_new[idx_min] = itm_max
array_new[idx_max] = itm_min

[print(f'{s:>4}', end='') for s in array]
print(f"\n{'-' * 40}")
[print(f'{s:>4}', end='') for s in array_new]
print(f"\n{'-' * 40}")
