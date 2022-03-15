# https://quera.org/problemset/10230/
# python 3.10.2
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a == 0 or b == 0 or c == 0:
    print("No")
elif a+b+c == 180:
    print("Yes")
else:
    print("No")
