# https://quera.org/problemset/17675/
# python 3.10.2
num=int(input())
fibonacci=[1,1]
for i in range(num-2):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
for i in range(1,num+1):
    if i in fibonacci:
        print("+",end='')
    else:
        print("-",end='')