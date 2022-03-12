a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))
c = int(input("Введите целое число c: "))
if a > b:
    if a > c:
        print(f"Максимальное число: {a}")
elif b < c:
    print(f"Максимальное число: {c}")
else:
    print(f"Максимальное число: {b}")
