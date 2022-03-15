# https://quera.org/problemset/3538/
# python 3.10.2
days = ["shanbe", "1shanbe", "2shanbe","3shanbe", "4shanbe", "5shanbe", "jome"]
num_1 = int(input())
string_1 = input().split()
num_2 = int(input())
string_2 = input().split()
num_3 = int(input())
string_3 = input().split()
for string in [string_1, string_2, string_3]:
    for i in range(len(string)):
        if string[i] in  days  :
            days.remove(string[i])
print(len(days))
