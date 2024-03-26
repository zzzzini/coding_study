n, l = map(int, input().split())
loc = sorted(list(map(int, input().split())))
cnt = 0
length = 1
for i in range(len(loc)):
    if i == 0:
        cnt += 1
    else:
        temp = loc[i] - loc[i-1]
        if length + temp > l:
            cnt += 1
            length = 1
        else:
            length += temp

print(cnt)