for i in range(0,3,1):
    lst = list(map(int, input().split()))
    cnt = 0
    for j in range(0,4,1):
        if lst[j] == 0:
            cnt += 1
    if cnt == 0:
        print("E")
    elif cnt == 1:
        print("A")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("C")
    elif cnt == 4:
        print("D")