def cego(i,j):
    S = 0
    if i in range(1,7) and j in range(1,4):
        S = pow(i,j)
        print(S)

    elif i in range(8,20) and j in range(8,20):
        S = i - j
        print("|i - j| = ", abs(S))
    else:
        print("ощибочка")


a = int(input("Введите i :"))
b = int(input("Введите j :"))

cego(a,b)





