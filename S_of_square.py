import math
def sum(x1,x2,y1,y2):
    res=(x1+x2)**2+(y1+y2)**2
    sqrt= math.sqrt(res)
    Sum = sqrt ** 2 / 2
    return Sum
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
Sum = sum(x1,x2,y1,y2)
