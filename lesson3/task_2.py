import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

arr_below = []
arr_larger = []

for item in array:

    if item > 0:
        arr_larger.append(item)
    elif item < 0:
        arr_below.append(item)

print(arr_below)
print(arr_larger)

# Использование list comprehension
# менее эфективно чем первый вариант в два раза
# за счет прохода по списку дважды(в arr_below1 и arr_larger1)

arr_below1 = [item for item in array if item < 0]
arr_larger1 = [item for item in array if item > 0]
print(arr_below1)
print(arr_larger1)
