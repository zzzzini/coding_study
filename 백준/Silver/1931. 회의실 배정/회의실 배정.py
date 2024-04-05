li = []
for i in range(int(input())):
    li.append(list(map(int, input().split())))
li.sort(key=lambda x: (x[1],x[0]))

pointer = 0
cnt = 0
for item in li:
    if item[0] >= pointer:
        cnt += 1
        pointer = item[1]
print(cnt)