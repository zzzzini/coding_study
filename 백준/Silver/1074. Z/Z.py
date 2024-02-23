n, r, c = map(int, input().split())
cnt = 0

while n > 0:
    n -= 1
    square = (2**n) * (2**n)

    if r < 2**n and c < 2**n:
        cnt += 0
    elif r < 2**n and c >= 2**n:
        cnt += square
        c -= (2**n)
    elif r >= 2**n and c < 2**n:
        cnt += (square*2)
        r -= (2**n)
    else:
        cnt += (square*3)
        r -= (2**n)
        c -= (2**n)

print(cnt)