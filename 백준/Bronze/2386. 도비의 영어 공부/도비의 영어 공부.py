while True:
    s = input().lower()
    c = s[0]
    cnt = 0
    if s == "#":
        break
    for i in range(2,len(s),1):
        if s[i] == c:
            cnt += 1
    print(c, cnt)