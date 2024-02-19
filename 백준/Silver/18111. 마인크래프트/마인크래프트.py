import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

mintime = 500*500*256*2
minheight = 256

for i in range(257):
    one = 0
    two = 0

    for r in range(n):
        for c in range(m):
            if li[r][c] > i:
                one += (li[r][c] - i)
            else:
                two += (i - li[r][c])

    if b >= two - one:
        time = (one * 2) + (two * 1)
        mintime = min(mintime, time)

        if time == mintime:
            minheight = i

print(mintime, minheight)