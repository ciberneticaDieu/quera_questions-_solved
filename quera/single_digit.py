# https://quera.org/problemset/3539/
# python 3.10.6
num = input()
while len(num) > 1:
    num = str(sum([int(j) for j in num]))
print(num)