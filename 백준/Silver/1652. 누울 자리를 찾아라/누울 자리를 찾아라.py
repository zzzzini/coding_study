n = int(input())
room = []
for i in range(n):
    room.append(list(input()))

row = []
for item in room:
    temp = ''
    for items in item:
        if items == '.':
            temp += items
        else:
            row.append(temp)
            temp = ''
    row.append(temp)

rcnt = len([k for k in row if len(k) >= 2])

croom = [list(k) for k in zip(*room)]
col = []
for item in croom:
    temp = ''
    for items in item:
        if items == '.':
            temp += items
        else:
            col.append(temp)
            temp = ''
    col.append(temp)

ccnt = len([k for k in col if len(k) >= 2])

print(rcnt, ccnt)