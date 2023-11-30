n = int(input())
for i in range(0,n,1):
    a, b = map(int, input().split())
    num = a * b
    while b != 0:
        r = a % b
        a = b
        b = r
    num /= a
    print(int(num), a)