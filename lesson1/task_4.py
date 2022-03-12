a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))
c = int(input("Введите целое число c: "))
m = a
if m < b:
    m = b
if m < c:
    m = c
print(f"Максимальное число: {m}")
