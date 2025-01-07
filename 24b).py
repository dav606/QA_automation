n = 8
s = "".join(str(i) for i in range(n,0,-1))
for i in range(n, 0, -1):
    print(s[:i])
