# https://quera.org/problemset/49535/
# python 3.10.2
n,v=input().split()
n=int(n)
v=int(v)
limit=[]
for i in range(n):
    I=int(input())
    limit.append(I)
if sum(limit) >= v:
    print("YES")
else:
    print("NO")
    