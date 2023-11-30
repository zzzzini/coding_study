s = input()
check = 0
if len(s) % 2 == 0:
    half = len(s) // 2
    for i in range(0, half, 1):
        if s[i] == s[len(s)-(i+1)]:
            check += 1
    if check == half:
        print(1)
    else:
        print(0)
else:
    half = len(s) // 2
    for i in range(0, half, 1):
        if s[i] == s[len(s)-(i+1)]:
            check += 1
    if check == half:
        print(1)
    else:
        print(0)