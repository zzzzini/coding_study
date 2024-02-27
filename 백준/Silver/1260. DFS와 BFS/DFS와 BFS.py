n, m, v = map(int, input().split())
li_dfs = [[] for i in range(n)]
li_bfs = [[] for i in range(n)]
for i in range(m):
    l, r = map(int, input().split())
    if r not in li_dfs[l-1]:
        li_dfs[l-1].append(r)
        li_bfs[l-1].append(r)
    if l not in li_dfs[r-1]:
        li_dfs[r-1].append(l)
        li_bfs[r-1].append(l)

for item in li_dfs:
    item.sort()

for item in li_bfs:
    item.sort()

need_visit = []
visited = []
need_visit.append(v)

while need_visit:
    node = need_visit.pop(0)
    if node not in visited:
        visited.append(node)
        li_dfs[node-1].extend(need_visit)
        need_visit = li_dfs[node-1]

for item in visited:
    print(item, end=' ')
print()

need_visit = []
visited = []
need_visit.append(v)

while need_visit:
    node = need_visit.pop(0)
    if node not in visited:
        visited.append(node)
        need_visit.extend(li_bfs[node-1])

for item in visited:
    print(item, end=' ')