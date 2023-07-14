a = int(input())
b = int(input())
c = int(input())
if c > a * b:
    print("no")
elif c % a == 0 or c % b == 0:
    print("yes")
else:
    print("no")