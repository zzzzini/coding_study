n = int(input())
stu = []
cnt = [0 for i in range(n)]
for i in range(n):
    stu.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(5):
            if stu[i][k] == stu[j][k]:
                cnt[i] += 1
                break

print(cnt.index(max(cnt))+1)