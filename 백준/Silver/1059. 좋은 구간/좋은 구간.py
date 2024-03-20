l = int(input())
s = list(map(int, input().split()))
n = int(input())

maxmin = 1
minmax = 1000
s.sort()
for item in s:
    if item <= n:
        maxmin = max(maxmin, item)
    elif item >= n:
        minmax = min(minmax, item)

cnt = 0

if maxmin in s:
    maxmin += 1

for i in range(maxmin, n+1):
    for j in range(n, minmax):
        if i==j:
            continue
        cnt += 1

print(cnt)