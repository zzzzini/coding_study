n = int(input())
l = []
for i in range(n):
    w = list(map(int, input().split()))
    l.append(w)

rank = [1 for i in range(n)]

for i in range(n):
    counter = 0
    for j in range(n):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            counter += 1
    rank[i]+=counter

for i in rank:
    print(i, end = ' ')