import math

def triangle(x1,y1,x2,y2,x3,y3):
  res1 = (x1-x2)**2 + (y1-y2)**2
  a = math.sqrt(res1)
  res2 = (x2-x3)**2 + (y2-y3)**2
  b = math.sqrt(res2)
  res3 = (x3-x1)**2 + (y3-y1)**2
  c=math.sqrt(res3)
  p=(a+b+c)/2
  RES=p*(p-a)*(p-b)*(p-c)
  S=math.sqrt(RES)
  return S

x1 = int(input("Enter X of A: "))
y1 = int(input("Enter Y of A: "))

x2 = int(input("Enter X of B: "))
y2 = int(input("Enter Y of B: "))

x3 = int(input("Enter X of C: "))
y3 = int(input("Enter Y of C: "))

S = triangle(x1,y1,x2,y2,x3,y3)

print(S)
