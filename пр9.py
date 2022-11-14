try:
    with open("peskova_ub22_input.txt") as f:
        matrix = [[int(x) for x in row.split()] for row in f]
        
    with open("peskova_ub22_output.txt", 'w') as f1:
        k = int(input('k = '))
        c, c_mas = 0, []
        c = 0
        for row in matrix:
            for el in row:
                if el % k == 0:
                    c += 1
                    c_mas.append(el)
        c = str(c)
        
        for i in c_mas:
            f1.write(str(i))
        f1.write(f"\n{c}")
finally:
    print('Success')