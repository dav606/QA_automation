n=int(input())

for i  in range(n+1):
    for j in range(8,i,-1):
        print(j, sep=' ' ,end= ' ' )
    print("\n")    