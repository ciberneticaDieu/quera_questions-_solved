# https://quera.org/problemset/20256/
# python 3.10.2
I = input()
G = I.count('G')
Y = I.count('Y')
R = I.count('R')
if R >= 3 or Y == 5:
    print("nakhor lite")
elif R >= 2 and Y >= 2:
    print("nakhor lite")
elif G == 0:
    print("nakhor lite")
else:
    print("rahat baash")
