import random as rd

n = int(input("Enter any len mas : "))
mas_1 = [rd.randint(1, 100) for i in range(n)]
mas_2 = [rd.randint(1, 100) for j in range(n)]
mas_3 = [rd.randint(1, 100) for k in range(n)]
print(mas_1, mas_2, mas_3, sep='\n')

prod = lambda arr:arr[0] * prod(arr[1:]) if arr else 1

def average_mean(x):
    return sum(x) / len(x)

print(f"Произведение 1-го = {prod(mas_1)},\n 2-го = {prod(mas_2)},\n 3-го = {prod(mas_3)} \
    \nСреднее 1-го = {average_mean(mas_1)},\n 2-го = {average_mean(mas_2)},\n 3-го = {average_mean(mas_3)}")
