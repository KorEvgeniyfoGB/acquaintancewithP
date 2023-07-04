a = input()
if len(a) % 2 == 0:
    d = 0
    e = 0
    for i in range(len(a)):
        if i >= (len(a) / 2):
            d += int(a[i])
        else:
            e += int(a[i])
    if d == e:
        print("yes")
    else:
        print("no")
else:
    print("not lucky")
