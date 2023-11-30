n, m = map(int,input().split())
a = []
for i in range(1,n+1,1):
    a.append(i)
for i in range(0,m,1):
    f, b = map(int,input().split())
    for j in range(f-1,b-1,1):
        for k in range(j+1,b,1):
            a[j],a[k] = a[k], a[j]
for i in range(0,n,1):
    print(a[i], end=' ')