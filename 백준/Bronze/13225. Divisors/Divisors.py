t = int(input())
for i in range(0,t,1):
    n = int(input())
    k = []
    if n == 1:
        k = [1]
    for j in range(1,n//2 + 1,1):
        if n % j == 0 and j not in k:
            k.append(j)
            if j != n//j:
                k.append(n//j)
    print(n,len(k))