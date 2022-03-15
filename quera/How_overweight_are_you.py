# https://quera.org/problemset/3404/
# python 3.10.2
weight = int(input())
high = float(input())
bmi = (weight/(high**2))
bmi = round(bmi, 2)
print(f"{bmi:2.2f}")
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
elif 30 <= bmi:
    print("Obese")
