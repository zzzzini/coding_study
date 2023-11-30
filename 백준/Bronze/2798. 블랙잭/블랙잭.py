n, m = map(int,input().split())
a = list(map(int, input().split()))
max = 0
temp = 0
for i in range(0,n-2,1):
    for j in range(i+1,n-1,1):
        for k in range(j+1,n,1):
            temp = a[i] + a[j] + a[k]
            if max < temp <= m:
                max = temp
print(max)