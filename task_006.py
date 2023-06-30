a = int(input())
b = 0
c = 0
while a > 999:
    c += a % 10
    a //= 10
while a != 0:
    b += a % 10
    a //= 10
if c == b:
    print("YES")
else:
    print("NO")