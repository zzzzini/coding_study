while True:
    line = list(map(int, input().split()))
    if line == [0]:
        break
    else:
        k = 1
        for i in range(1,len(line),2):
            n_line = line[i:i+2]
            k = (k * n_line[0] - n_line[1])
        print(k)