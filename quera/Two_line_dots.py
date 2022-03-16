# https://quera.org/problemset/3414/
# python 3.10.2
map1 = input().split()
if int(map1[0]) == int(map1[2]):
    print("Vertical")
elif int(map1[1]) == int(map1[3]):
    print("Horizontal")
else:
    print("Try again")