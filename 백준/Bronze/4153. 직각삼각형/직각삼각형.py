while True:
    line = list(map(int, input().split()))
    if line[0] == 0 and line[1] == 0 and line[2] == 0:
        break
    max = line[0]
    for i in range(1,3,1):
        if line[i] > max:
            max = line[i]
    if line[0] == max:
        if line[1] ** 2 + line[2] ** 2 == line[0] ** 2:
            print("right")
        else:
            print("wrong")
    if line[1] == max:
        if line[0] ** 2 + line[2] ** 2 == line[1] ** 2:
            print("right")
        else:
            print("wrong")
    if line[2] == max:
        if line[0] ** 2 + line[1] ** 2 == line[2] ** 2:
            print("right")
        else:
            print("wrong")