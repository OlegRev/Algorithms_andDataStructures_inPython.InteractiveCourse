"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
import random

array = [random.randint(0, 10) for _ in range(10)]
array_new = array[:]

itm_min1 = float('inf')
itm_min2 = float('inf')
for idx, itm in enumerate(array_new):
    if itm < itm_min1:
        itm_min1 = itm
        idx_min1 = idx

"""
Удаление и замена на максимальное число для формирования вывода:

Массив array: [5, 6, 6, 10, 10, 4, 5, 0, 5, 0]
----------------------------------------
Первое минимальное число в массиве array[7]: 0
Второе минимальное число в массиве array[9]: 0

"""
array_new.pop(idx_min1)
array_new.insert(idx_min1, float('inf'))

for idx, itm in enumerate(array_new):
    if itm < itm_min2:
        itm_min2 = itm
        idx_min2 = idx

print(f"Массив array: {array}\n{'-' * 40}\n"
      f"Первое минимальное число в массиве array[{idx_min1}]: {itm_min1}\n"
      f"Второе минимальное число в массиве array[{idx_min2}]: {itm_min2}\n")
