"""5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте
«минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.

В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве
несколько раз, используйте один любой по вашему выбору.
"""
import random

array = [random.randint(-10, 10) for _ in range(30)]
max_negative_itm = 0
min_negative_itm = float('-inf')
for idx, itm in enumerate(array):
    if itm < 0:
        if itm > min_negative_itm:
            min_negative_itm = itm
            idx_min_neg = idx
        if itm < max_negative_itm:
            max_negative_itm = itm
            idx_max_neg = idx

print(f"Максимальный отрицательный элемент: {max_negative_itm}\n"
      f"в массиве находится под индексом: {idx_max_neg}\n\n"
      f"Минимальный отрицательный элемент: {min_negative_itm}\n"
      f"в массиве находится под индексом: {idx_min_neg}\n"
      f"{'-' * 10}\nМассив:\n{array}")
