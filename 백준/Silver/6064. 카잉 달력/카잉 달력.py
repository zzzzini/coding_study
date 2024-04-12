n = int(input())
for i in range(n):
    m, n, x, y = map(int, input().split())
    month, day = 1, 1
    count = x
    flag = False

    while count <= m * n:
        if (count - x) % m == 0 and (count - y) % n == 0:
            flag = True
            break

        count = count + m

    if flag:
        print(count)
    else:
        print(-1)