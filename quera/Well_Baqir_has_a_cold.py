# https://quera.org/problemset/10231/
# python 3.10.2
number_line = []
r = 5
for i in range(r):
    string = input()
    if "MOLANA" in string or "HAFEZ" in string:
        number_line.append(i+1)
# " ".join(number_line) if len(number_line)>0 else "NOT FOUND!"
string_dup = ''.join(str(number_line).split(','))
print(str(string_dup)[1:-1])
