n = int(input())
m = int(input())
k = int(input())
if k > m * n:
    print("NO")
elif k % m == 0 or k % n == 0:
    print("YES")
else:
    print("NO")