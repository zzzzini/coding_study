l = int(input())
b = list(map(int,input().split()))
a = [1] * l
c = []
for i in range(l-1,-1,-1):
    a[i] = b[i] * (i+1)
c = [a[0]]
for i in range(1,l,1):
    c.append(a[i] - a[i-1])
for i in range(0,l,1):
    print(c[i], end=' ')