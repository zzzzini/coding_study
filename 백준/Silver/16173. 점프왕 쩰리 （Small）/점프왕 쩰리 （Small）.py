import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
node = [[0 for i in range(n)] for j in range(n)]

def dfs(x,y):
    global node
    if x >= n or y >= n or node[x][y] == 1:
        return

    move = board[x][y]
    if move == -1:
        node[x][y] = 1
        return

    node[x][y] = 1
    dfs(x,y+move)
    dfs(x+move,y)

dfs(0,0)
if node[n-1][n-1] == 1:
    print("HaruHaru")
else:
    print("Hing")