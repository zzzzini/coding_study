n, k = map(int,input().split())
dell = []
for i in range(2,n+1,1):
    if i not in dell:
        dell.append(i)
    for t in range(2,n+1,1):
        if t % i == 0 and t not in dell:
            dell.append(t)
print(dell[k-1])