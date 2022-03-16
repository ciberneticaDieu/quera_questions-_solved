# https://quera.org/problemset/293/
# python 3.10.2
num1 = int(input())
num2 = int(input())
prime = []
for i in range(num1, num2+1):
    d = []
    n = 1
    while n < i+1 :
        if i % n == 0:
            d.append(n)
        n += 1
    if len(d) == 2:
        prime.append(i)
    else:
        pass
prime = str(prime).replace("[", "")
prime = str(prime).replace("]", "")
prime = str(prime).replace(" ", "")
prime = str(prime).replace(",", "\n")
print(prime)