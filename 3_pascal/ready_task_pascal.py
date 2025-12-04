# вывод отформатированного треугольника паскаля

# до 4 уровня включительно

level = int(input('Введите уровень треугольника Паскаля: '))

pascal = {}
for i in range(level):
    list=[1]
    for k in range(1,i):
        n1 = int (pascal[i-1][k-1])
        n2 = int( pascal[i-1][k])
        list.append(n1 + n2)
    if i>0:
        list.append(1)
    pascal[i]= list





for lev in pascal.keys():
    row = pascal[lev]
    b = level - lev
    print(" " * b ,row)







