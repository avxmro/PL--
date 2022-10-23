import random as rd

n, kk = 6, 6
matrix = []
for r in range(n):
    b = []
    for c in range(kk):
        b.append(rd.randint(1, 10))
    matrix.append(b)
print(matrix)

k = int(input('k = '))
c, c_mas = 0, []
def contains_1(matrix):
    c = 0
    for row in matrix:
        for el in row:
            if el % k == 0:
                c += 1
                c_mas.append(el)
    return c, c_mas

print(contains_1(matrix))
print(c_mas)
