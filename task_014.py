n = int(input("Введите число до которого вы хотели бы видеть степени двойки: "))
t = 0
while 2 ** t < n:
    print(2 ** t, end=" ")
    t += 1