# https://quera.org/problemset/3406/
# python 3.10.2
a = input()
b = input()
if a == b:
    print(a, "=", b)
elif int(a[::-1]) > int(b[::-1]):
    print(b, "<", a)
else:
    print(a, "<", b)