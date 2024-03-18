import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
li = []
x = 0
y = 0
count = 0
for i in range(n):
    line = input()
    if 'I' in line:
        x = i
        y = line.index('I')
    li.append(line)

visit = [[True for i in range(m)] for j in range(n)]
movex = [-1,1,0,0]
movey = [0,0,-1,1]

def dfs(x,y):
    global count
    visit[x][y] = False

    if li[x][y] == "P":
        count += 1

    for i in range(4):
        dx = x + movex[i]
        dy = y + movey[i]
        if 0 <= dx < n and 0 <= dy < m and visit[dx][dy]:
            if li[dx][dy] != "X":
                dfs(dx,dy)

dfs(x,y)
if count > 0:
    print(count)
else:
    print("TT")