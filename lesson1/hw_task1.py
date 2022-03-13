"""
1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""
a = 5
b = 6
print(f'bit_and(5 & 6) = {a & b}')
print(f'bit_or(5 | 6) = {a | b}')
print(f'bit_xor(5 ^ 6) = {a ^ b}')
print(f'inversion_a(~5) = {~a}')
print(f'inversion_b(~6) = {~b}')
print(f'bit_shift_right(5 >> 2) = {a >> 2}')
print(f'bit_shift_left(5 << 2) = {a << 2}')
