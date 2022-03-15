# https://quera.org/problemset/3403/
# python 3.10.2
I_1 = int(input())
I_2 = int(input())
I_3 = int(input())
I_4 = int(input())
I = [I_1, I_2, I_3, I_4]
Product = I_1*I_2*I_3*I_4
print(f"Sum : {sum(I):.6f}\nAverage : {sum(I)/len(I):.6f}\nProduct : {Product:.6f}\nMAX : {max(I):.6f}\nMIN : {min(I):.6f}")
