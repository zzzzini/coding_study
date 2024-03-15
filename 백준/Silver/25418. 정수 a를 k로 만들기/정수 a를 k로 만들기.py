a, k = map(int, input().split())

visit = list()
visited = dict()

visit.append(a)
visited[a] = 0

while visit:

    node = visit.pop(0)
    if node == k:
        print(visited[node])
        break

    one = node + 1

    if one <= k and one not in visited.keys():
        visited[one] = visited[node] + 1
        visit.append(one)

    double = node * 2

    if double <= k and double not in visited.keys():
        visited[double] = visited[node] + 1
        visit.append(double)