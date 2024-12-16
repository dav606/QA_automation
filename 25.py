n=int(input())

for i in range(n+1):
    print(" " * ( n + 1 - i), end="")
    if i % 2 :
        print(int(i/2), end="")
        for  j in range(int(i/2)+1, i):    
            print(f"{j}{j}", end="")
        print(i)    
    if not i% 2:            
        for  j  in range(int(i/2), i):
            if i:    
                print(f"{j}{j}", end="")
        print(i)
    print()    
           

