n = list(map(int, input().split()))
tmp = 0
for i in range(0,2,1):
    for j in range(1,3,1):
        if n[i] > n[j]:
            tmp = n[i]
            n[i] = n[j]
            n[j] = tmp
for i in range(0,3,1):
    print(n[i], end=' ')