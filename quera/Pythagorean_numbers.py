# https://quera.org/problemset/280/
# python 3.10.2
a = int(input())
b = int(input())
c = int(input())
if a*a == b*b + c*c or b*b == c*c + a*a or c*c == a*a + b*b:
    print("YES")
else:
    print("NO")
