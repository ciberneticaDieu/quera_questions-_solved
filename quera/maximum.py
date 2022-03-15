# https://quera.org/problemset/588/
# python 3.10.2
I = int(input())
I_2 = input().split()
for i in range(len(I_2)):
    I_2[i] = int(I_2[i])
print(max(I_2))
