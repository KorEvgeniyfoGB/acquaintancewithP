n = [int(i) for i in input("Введите положение монет через пробел, 1 - решка или 0 - орел: ").split()]
a = n.count(1)
b = n.count(0)
if a > b:
    print(b)
elif b > a:
    print(a)
else:
    print("безразлично")