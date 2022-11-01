from random import randint
size = int(input("Введите размер матрицы:"))
minimum = int(input("Введите минимальное значение матрицы:"))
maximum = int(input("Введите максимальное значение матрицы:"))

a = [[randint(minimum,maximum) for j in range(size)] 
    for i in range(size)]
for row in a:
    print(*row)
    
amax = a[0][0]
imax = jmax = 0
for i in range(size):
    for j in range(size):
        if amax < a[i][j]:
            imax, jmax = i, j 
            amax = a[i][j]
print(amax)
 
a = [[a[i][j] for j in range(size) if j != jmax] 
    for i in range(size) if i != imax]
for row in a:
    print(*row)
