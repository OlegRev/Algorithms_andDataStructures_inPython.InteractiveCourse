"""
2. По введенным пользователем координатам двух точек вывести уравнение прямой
вида y = kx + b, проходящей через эти точки.
"""
x1, y1 = int(input('x1: ')), int(input('y1: '))
x2, y2 = int(input('x2: ')), int(input('y2: '))
k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
print(f'Уравнение прямой проходящей через точки:\n'
      f'А{x1, y1}, B{x2, y2}\n'
      f'Имеет вид y = kx + b где k = {k:.1f}, b = {b:.1f}')
