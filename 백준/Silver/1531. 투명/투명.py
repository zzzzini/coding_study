n, m = map(int, input().split())
board = [[0 for i in range(100)] for j in range(100)]
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    for l in range(lx-1, rx):
        for r in range(ly-1, ry):
            board[l][r] += 1

cnt = 0
for i in range(100):
    cnt += len([k for k, v in enumerate(board[i]) if v > m])
print(cnt)