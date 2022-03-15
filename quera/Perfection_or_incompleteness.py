# https://quera.org/problemset/282/
# python 3.10.2
Number = int(input())
counter = 1
sum = 0
while counter < Number:
    if Number % counter == 0:
        sum += counter
    counter += 1
if sum == Number:
    print("YES")
else:
    print("NO")
