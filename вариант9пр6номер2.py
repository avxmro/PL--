import random as rd

m = int(input('длина = '))
mas = []
mas = [int(input()) for _ in range(m)]

print(*mas)
mas.reverse()
print('реверснутый массив = ', mas)

mn = 100500
for i in range(m):
    if abs(mas[i]) < abs(mn):
        mn = mas[i]

print(f"минимальное по модулю : {mn}")

mas_a, mas_b = [rd.randint(-5, 5) for j in range(10)], [rd.randint(-5, 5) for k in range(10)]
print(mas_a, mas_b, sep='\n')
mas_a, mas_b = mas_b, mas_a
print(f"Массив а после обработки : {mas_a},\n и массив b : {mas_b}")
