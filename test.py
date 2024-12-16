#erankyun
number = input("Enter number - ")
rows = int(number)

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print(" ")


#24/a

number = input("Enter number - ")
rows = int(number)

for i in range(rows,0,-1):
    for j in range(i):
        print("0 ", end="")
    print("")


#24/b

number = input("Enter number - ")
rows = int(number)

for i in range(rows,0,-1):
    for j in range(rows, rows - i,-1):
        print( j ," ", end="")
    print("")

#24/g


number = input("Enter number - ")
rows = int(number)

for i in range(2,9):
    for j in range(i,9):
        print( j ," ", end="")
    print("")



#25

for i in range(10):

    print((10 - i) * " ", end="")

    if i % 2 == 0:
        for j in range(i // 2, i + 1):
            if j == i:
                print(str(j), end="")
            else:
                print(2 * str(j), end="")
    else:
        for j in range(i // 2, i + 1):
            if j == (i // 2) or j == i:
                print(str(j), end="")
            else:
                print(2 * str(j), end="")
    print()
