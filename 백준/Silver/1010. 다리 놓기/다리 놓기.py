def rec(n, m, diff):
    if m == diff:
        return 1
    else:
        return m * rec(n, m-1, diff)

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(rec(n,m,m-n) // fact(n))