num = int(input())
for i in range(0,num,1):
    n = int(input())
    w = 0
    for j in range(2,n+2,1):
        t = 0
        for k in range(1,j+1,1):
            t += k
        w += (j-1) * t
    print(w)