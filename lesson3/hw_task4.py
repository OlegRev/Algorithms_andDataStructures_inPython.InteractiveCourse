"""4. Определить, какое число в массиве встречается чаще всего.

В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве
несколько раз, используйте один любой по вашему выбору.
"""
import random

array = [random.randint(0, 10) for _ in range(30)]
frequent_num = 0
max_count = 0

for itm in array:
    count_num = 0
    for i in array:
        if itm == i:
            count_num += 1
    if count_num > max_count:
        max_count = count_num
        frequent_num = itm


print(f"Число {frequent_num} чаще всего встречается в массиве:\n"
      f"количество раз: {max_count}\n"
      f"{array}\n{'--' * 50}")

# через функцию count()
frequent_number = 0

for itm in array:
    if array.count(itm) > array.count(frequent_number):
        frequent_number = itm

print(f"Число {frequent_number} чаще всего встречается в массиве:\n"
      f"количесвто раз: {array.count(frequent_number)}\n"
      f"{array}")
