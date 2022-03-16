# https://quera.org/problemset/35253/
# python 3.10.2
num = int(input())
w = (input().split())
for i in range(len(w)):
    w[i] = int(w[i])
print(w.index(max(w))+1)
