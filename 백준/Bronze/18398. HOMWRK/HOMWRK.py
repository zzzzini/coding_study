n = int(input())
for i in range(0, n, 1):
    t = int(input())
    for j in range(0, t, 1):
        a, b = map(int, input().split())
        print(a+b, a*b)