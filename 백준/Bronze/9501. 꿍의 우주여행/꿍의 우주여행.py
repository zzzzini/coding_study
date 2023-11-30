k = int(input())
for i in range(0,k,1):
    n, d = map(int, input().split())
    cnt = 0
    for j in range(0,n,1):
        v, f, c = map(int, input().split())
        time = d // v
        left = d % v
        gap = left / v
        if (time + gap) * c <= f:
            cnt += 1
    print(cnt)