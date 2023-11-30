a = list(map(int, input().split()))
tmp = 0
for i in range(0,2,1):
    for j in range(1,3,1):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
print(a[1])