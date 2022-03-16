# https://quera.org/problemset/2659/
# python 3.10.2
num = int(input())
string1 = str(input())
string2 = str(input())
n = 0
for i in range(len(string1)):
    for x in string1[i]:
        for y in string2[i]:
            if y == x:
                pass
            else:
                n += 1
print(n)