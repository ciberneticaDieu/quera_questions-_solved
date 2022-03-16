# https://quera.org/problemset/6082/
# python 3.10.2
I = input().split()
I[0] = int(I[0])
I[1] = int(I[1])
x = []
for i in range(I[0]):
    x.append(input().count("*"))
print(sum(x))
