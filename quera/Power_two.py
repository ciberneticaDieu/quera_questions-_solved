# https://quera.org/problemset/616/
# python 3.10.2
number = int(input())
power = 2
while number != power:
    power *= 2
    if power >= number:
        print(power)
        break
