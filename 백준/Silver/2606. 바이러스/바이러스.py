n = int(input())
m = int(input())
dict = {k:set() for k in range(1,n+1)}
for i in range(m):
    start, end = map(int, input().split())
    dict[start].add(end)
    dict[end].add(start)

visited = []
def dfs(node):
    global visited
    for item in dict[node]:
        if item not in visited:
            visited.append(item)
            dfs(item)

dfs(1)
visited = [k for k in visited if k != 1]
print(len(visited))