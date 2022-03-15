# https://quera.org/problemset/2636/
# python 3.10.2
parts = input().split()
keeper = []
i = 0
while i < len(parts):
    if i < 2:
        keeper.append(str(1-int(parts[i])))
    elif i < 5:
        keeper.append(str(2-int(parts[i])))
    else:
        keeper.append(str(8-int(parts[i])))
    i += 1
print(" ".join(keeper))
