n, k, l = map(int,(input().split()))
new = []
count = 0
for i in range(0,n,1):
    team = list(map(int,input().split()))
    cnt = 0
    for each in team:
        if each >= l:
            cnt += 1
    if cnt == 3 and sum(team) >= k:
        count += 1
        for j in range(0,3,1):
            new.append(team[j])
print(count)
for i in range(0,len(new),1):
    print(new[i], end=' ')