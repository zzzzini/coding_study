k, n = map(int,input().split())
if n == 1:
    print(-1)
else:
    t = n*k // (n-1)
    if n*k % (n-1) == 0:
        print(t)
    else:
        print(t+1)