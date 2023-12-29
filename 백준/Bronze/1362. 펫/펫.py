no = 1
while True:
    o, w = map(int, input().split())
    status = 1
    if o == 0 and w == 0:
        break

    while True:
        action, num = input().split()
        num = int(num)
        if action == '#' and num == 0:
            break

        if action == "E" and status == 1:
            w -= num
        elif action == "F" and status == 1:
            w += num

        if w <= 0:
            status = 0

    if w > 0.5 * o and w < 2 * o:
        print(no, ":-)")
    elif w <= 0:
        print(no, "RIP")
    else:
        print(no, ":-(")

    no += 1