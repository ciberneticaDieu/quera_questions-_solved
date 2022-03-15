# https://quera.org/problemset/4065/
# python 3.10.2
number = input().split(" ")
a, b, l = int(number[0]), int(number[1]), int(number[2])
count = 1
sums = 0
while count <= l:
    if count % 2 != 0:
        sums += a
    else:
        sums += b
    count += 1
print(sums)
