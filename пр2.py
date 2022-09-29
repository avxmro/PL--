import math
x=int(input("Введите переменную x:"))
y=int(input("Введите переменную y:"))
z=int(input("Введите переменную z:"))
s=abs(x**(y/x))-(math.pow(y/z,[3])+(y-x))*((math.cos(y)-(z/(y-x)))/(1+(y-x)**2))
