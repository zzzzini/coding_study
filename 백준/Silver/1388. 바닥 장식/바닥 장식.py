li = []
n, m = map(int, input().split())
for i in range(n):
    li.append(input())

cnt = 0
for i in range(n):
    for j in range(m-1):
        if li[i][j] == '-':
            if li[i][j+1] == '|':
                cnt += 1
    if li[i][m-1] == '-':
        cnt += 1

for i in range(m):
    for j in range(n-1):
        if li[j][i] == '|':
            if li[j+1][i] == '-':
                cnt += 1
    if li[n-1][i] == '|':
        cnt += 1

print(cnt)