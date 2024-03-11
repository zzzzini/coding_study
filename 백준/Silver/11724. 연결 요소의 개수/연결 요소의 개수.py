import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
dict = {k+1:[] for k in range(n)}
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    dict[u].append(v)
    dict[v].append(u)

visited = []

def dfs(start):
    if start not in visited:
        visited.append(start)
    for item in dict[start]:
        if item not in visited:
            dfs(item)

cnt = 0
while True:
    if len(visited) == n:
        break
    ways = [k for k in dict.keys() if k not in visited]
    dfs(ways[0])
    cnt += 1
print(cnt)