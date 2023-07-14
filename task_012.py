s = int(input())
p = int(input())
for i in range(1001):
    for j in range(1001):
        if i + j == s and i * j == p:
            print(i, j)
            break