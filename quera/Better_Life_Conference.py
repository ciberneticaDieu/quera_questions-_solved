# https://quera.org/problemset/10325/
# python 3.10.2
r, c = input().split()
r = int(r)
c = int(c)
if c <= 10:
    print('Right', 11 - r, c)
else:
    print('Left', 11 - r, 21 - c)
