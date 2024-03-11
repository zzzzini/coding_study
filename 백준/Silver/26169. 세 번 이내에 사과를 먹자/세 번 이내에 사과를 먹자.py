board = []
for i in range(5):
    board.append(list(map(int, input().split())))

r, c = map(int, input().split())
bool = False

def dfs(r,c,move,cnt):
    global bool

    cnt = cnt
    if r > 4 or c > 4 or r < 0 or c < 0 or move > 3:
        return

    if board[r][c] == -1:
        return

    if board[r][c] == 1:
        cnt += 1

    temp = board[r][c]
    board[r][c] = -1

    if cnt == 2:
        bool = True
        return

    dfs(r+1, c, move+1, cnt)
    dfs(r-1, c, move+1, cnt)
    dfs(r, c+1, move+1, cnt)
    dfs(r, c-1, move+1, cnt)

    board[r][c] = temp

dfs(r,c,0,0)
if bool:
    print(1)
else:
    print(0)