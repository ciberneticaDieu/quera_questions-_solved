# https://quera.org/problemset/2794/
# python 3.10.2
a = input().split()
b = input().split()
c = input().split()
x = [a[0], b[0], c[0]]
for i in set(x):
    if x.count(i) == 1:
        x = i
y = [a[1], b[1], c[1]]
for i in set(y):
    if y.count(i) == 1:
        y = i
print(x, y)