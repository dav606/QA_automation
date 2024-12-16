n = 9
s = "".join(str(i) for i in range(2,n+1))
for i in range(1,n):
    print(s[:i])
