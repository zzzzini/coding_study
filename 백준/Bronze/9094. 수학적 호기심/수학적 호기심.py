n = int(input())
for i in range(0,n,1):
    n, m = map(int,input().split())
    cnt = 0
    for a in range(1,n-1,1):
        for b in range(a+1,n,1):
            t = (a ** 2 + b ** 2 + m) % (a * b)
            if t == 0:
                cnt += 1
    print(cnt)