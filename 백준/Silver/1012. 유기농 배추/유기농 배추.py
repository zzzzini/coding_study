import sys
sys.setrecursionlimit(10**6)
def dfs(y,x):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    if li[y][x] == 1:
        li[y][x] = 0
        dfs(y-1,x)
        dfs(y+1,x)
        dfs(y,x-1)
        dfs(y,x+1)
        return True
    return False

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    cnt = 0
    li = [[0 for i in range(m)] for j in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        li[y][x] = 1

    for r in range(n):
        for c in range(m):
            if dfs(r,c):
                cnt += 1
    print(cnt)