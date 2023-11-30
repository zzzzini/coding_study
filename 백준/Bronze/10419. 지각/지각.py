n = int(input())
for i in range(0,n,1):
    d = int(input())
    s = 0
    while (s+1) + (s+1)**2 <= d:
        s += 1
    print(s)