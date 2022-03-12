num = int(input("Введите трехзначное число: "))
a = num // 100
b = num % 100 // 10
c = num % 10
summa = a + b + c
mult = a * b * c
print(f"Сумма чисел введеного числа: {summa}\n"
      f"Произведение этих же чисел: {mult}")
