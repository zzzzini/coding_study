while True:
    num = input()
    edge = 0
    if num == "0":
        break
    else:
        for item in num:
            if item == '1':
                edge += 2
            elif item == '0':
                edge += 4
            else:
                edge += 3
        edge += (len(num)-1)
        edge += 2
    print(edge)