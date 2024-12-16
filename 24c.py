n=int(input())

for i  in range(n):
    for j in range(i+2,n+1):
        print(j, sep=' ' ,end= ' ' )
    print("\n")    