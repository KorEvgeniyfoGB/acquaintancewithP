# Задача 30:  Заполните список элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def ar_prog(a, b, c):
    res = [a + i * b for i in range(c)]
    return res


print(ar_prog(int(input()), int(input()), int(input())))