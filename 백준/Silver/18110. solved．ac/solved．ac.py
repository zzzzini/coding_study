import sys

input = sys.stdin.readline

n = int(input())
li = []
dict = {t: 0 for t in range(1, 31)}

if n == 0:
    print(0)

else:
    for i in range(n):
        k = int(input())
        li.append(k)
        dict[k] += 1

    d = round(n * 15 / 100 + 0.0000001)
    # n_li = li[d:-d]
    bottom = 0
    top = 0

    for i in range(1, 31):
        if bottom != d:
            while bottom != d and dict[i] != 0:
                bottom += 1
                dict[i] -= 1
        else:
            break

    for i in range(30, 0, -1):
        if top != d:
            while top != d and dict[i] != 0:
                top += 1
                dict[i] -= 1
        else:
            break

    sum = 0
    for i in range(1, 31):
        sum += (i * dict[i])

    print(round(sum / (n - 2 * d) + 0.0000001))