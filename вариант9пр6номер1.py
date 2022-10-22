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

print(mn)