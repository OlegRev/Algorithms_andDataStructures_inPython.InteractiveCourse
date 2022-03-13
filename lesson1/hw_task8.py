"""
8. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).
"""
a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))
if ((a > b) & (a < c)) | ((a < b) & (a > c)):
    median = a
elif ((b > a) & (b < c)) | ((b < a) & (b > c)):
    median = b
else:
    median = c
print(f'Медиана среди чисел {a, b, c} : {median}')
