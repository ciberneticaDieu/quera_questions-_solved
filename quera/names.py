# https://quera.org/problemset/2529/
# python 3.10.2
num = int(input())
names = []
alphabet = []
letter = []
for i in range(num):
    names.append(str(input()))
for i in range(num):
    alphabet.append(names[i])
for n in range(num):
    letter.append(len(set(alphabet[n])))
print(max(letter))