n = int(input())
for i in range(1, n + 1):
    t = i
    ds = i
    while True:
        ds += t % 10
        t = t // 10
        if t == 0: break
    if ds == n:
        print(i)
        break
    elif i == n:
        print(0)