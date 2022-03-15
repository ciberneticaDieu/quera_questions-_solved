# https://quera.org/problemset/3409/
# python 3.10.2
n = int(input())
i = 1
while i < n + 1:
    j = 1
    while j < n + 1:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1
