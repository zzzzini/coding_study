n = int(input())
for i in range(1,n+1,1):
    k = int(input())
    rooms = [1] * k
    for j in range(1,k+1,1):
        for t in range(1,k+1,1):
            if j % t == 0:
                rooms[j-1] = 1-rooms[j-1]
    cnt = 0
    for j in range(0,len(rooms),1):
        if rooms[j] == 0:
            cnt += 1
    print(cnt)