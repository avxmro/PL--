f=float(input('Введите первое число'))
v=float(input('Введите второе число'))
if f<4 and v>6:
    S=f+v
    print('if S=',S)
elif v<6:
    S=v**2
    print('elif S=',S)
else:
    S=2*v
    print('else S=',S)
