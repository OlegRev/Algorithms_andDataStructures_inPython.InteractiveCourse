# Цикл с предусловием
num = int(input('Введите целое число: '))
while num > 0:
    print(num % 10)
    num //= 10
