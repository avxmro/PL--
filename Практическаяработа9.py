try:

    with open("peskova_ub22_input.txt") as f:
        matrix = [[int(x) for x in row.split()] for row in f]
        
    with open("peskova_ub22_output.txt", 'w', encoding='utf-8') as f1:
        k = int(input('k = '))
        c_len = []
        c, c_mas = 0, []
        c = 0
        for row in matrix:
            for el in row:
                if el % k == 0:
                    c += 1
                    c_mas.append(el)
        c_len.append(c)
        c_max = max(c_mas)
        
        f1.write(f'Количество элементов: {str(*c_len)}\n')
        f1.write(f'Наибольший элемент из кратных k: {str(c_max)}\n')

        amax = matrix[0][0]
        imax = jmax = 0
        for i in range(6):
            for j in range(6):
                if amax < matrix[i][j]:
                    imax, jmax = i, j 
                    amax = matrix[i][j]
        
        matrix = [[matrix[i][j] for j in range(6) if j != jmax] 
            for i in range(6) if i != imax]
        
        f1.write('8.2 ниже\n')
        f1.write(f'Наибольший по модулю элемент матрицы: {amax}\n')
        f1.write('Ниже матрица порядка n-1\n')
        for y in matrix:
            f1.write(str(y))
        
finally:
    print('Success')


