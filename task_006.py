n = input()
if len(n) % 2 == 0:
    d = 0
    e = 0
    for i in range(len(n)):
        if i >= (len(n) / 2):
            d += int(n[i])
        else:
            e += int(n[i])
    if d == e:
        print("yes")
    else:
        print("no")
else:
    print("not lucky")
