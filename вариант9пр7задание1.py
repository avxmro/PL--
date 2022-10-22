n = int(input("Enter any len mas:"))
mas = [int(input()) for _ in range (n)]
print (*mas)

mn = 100500
for i in range (n):
    if abs(mas[i]) < abs(mn):
        mn = mas[i]

print (mn)
