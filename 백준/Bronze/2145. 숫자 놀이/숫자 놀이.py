while True:
    num = list(input())
    count = 0
    if num == ["0"]:
        break
    else:
        while True:
            if len(num) == 1:
                break
            else:
                s = sum(map(int, num))
                num = list(str(s))
        print(num[0])