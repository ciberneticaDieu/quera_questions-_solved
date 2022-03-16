num=int(input())
w=(input().split())
for i in range(len(w)):
    w[i]=int(w[i])
print(w.index(max(w))+1)