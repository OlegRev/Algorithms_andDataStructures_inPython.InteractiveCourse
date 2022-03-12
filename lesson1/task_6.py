num = float(input("Введите число: "))
ans = input(f"Перевести в байты - 'b'\n"
            f"Перевести в киолбайты - 'k'\n: ")
ans = ans.lower()
if ans == 'b':
    print(f"{num} Kб = {num * 1024} байт")
elif ans == 'k':
    print(f"{num} байт = {num / 1024} Кб")
else:
    print("Неверный ввод")
