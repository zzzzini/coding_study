n = int(input())
for i in range(0,n,1):
    n, d, a, b, f = map(float,input().split())
    k = d / (a+b) * f
    print(n, f'{k:.6f}')