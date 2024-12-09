
number = input("Enter number - ")
rows = int(number)

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print(" ")

