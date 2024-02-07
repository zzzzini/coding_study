from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(first):
    INF = float("inf")
    d = [INF] * (n+1)

    dq = deque()

    dq.append(first)
    d[first] = 0

    while dq:
        node = dq.popleft()
        for next in graph[node]:
            if d[next] == INF:
                d[next] = d[node] + 1
                dq.append(next)

    return d

result = [i for i,v in enumerate(bfs(x)) if v == k]

if len(result) == 0:
    print(-1)
else:
    while result:
        print(result.pop(0))