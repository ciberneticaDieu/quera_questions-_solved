# https://quera.org/problemset/3430/
# python 3.10.2
sound = input()
print(sound)
for i in range(1, len(sound)):
    print(sound[i]*i+sound[i:])
