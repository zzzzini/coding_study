t = int(input())
for i in range(t):
    input()
    a, b, c, d = map(int, input().split())

    li = [a,b,c]
    li.sort()

    small = li[0]
    mid = li[1]
    big = li[2]

    if big - mid >= d:
        print((big - d) * mid * small)

    elif big + mid - 2 * small >= d:
        if (big + mid - d) % 2 == 0:
            print(small * (((big + mid - d) // 2) ** 2))
        else:
            print(small * ((big + mid - d) // 2) * (((big + mid - d) // 2) + 1))

    else:
        cnt = d
        cnt -= (big - small)
        cnt -= (mid - small)

        if cnt % 3 == 0:
            print((small - (cnt // 3)) ** 3)
        elif cnt % 3 == 1:
            print(((small - (cnt // 3)) ** 2) * (small - (cnt // 3) - 1))
        else:
            print(((small - (cnt // 3)) * ((small - (cnt // 3) - 1)) ** 2))