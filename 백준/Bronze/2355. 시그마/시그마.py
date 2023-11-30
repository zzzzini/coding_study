a, b = map(int,input().split())
if a > b:
    a, b = b, a
len = b - a + 1
if len % 2 == 0:
    print((a+b) * len//2)
elif len % 2 == 1:
    print((a+b) * int(len//2) + (a + len//2))