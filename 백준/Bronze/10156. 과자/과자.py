k, n, m = map(int, input().split())
num = (k * n)
if num > m:
    print(num-m)
else:
    print(0)