"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.
"""
import random


def test_task2(array_test=[8, 3, 15, 6, 4, 2], true_array=[0, 3, 4, 5]):
    arr_test = []
    for idx, itm in enumerate(array_test):
        if itm % 2 == 0:
            arr_test.append(idx)
    if arr_test == true_array:
        print("TEST: PASSED")
    else:
        print("TEST: FAILED")


test_task2()

array = [random.randint(0, 100) for _ in range(10)]
array_2 = []
for idx, itm in enumerate(array):
    if itm % 2 == 0:
        array_2.append(idx)

print(array, array_2, end='\n')
