while True:
    s = input().lower()
    cnt = 0
    if s == '#':
        break
    for i in range(0,len(s),1):
        if s[i] == 'a' or s[i] == 'i' or s[i] == 'e' or s[i] == 'o' or s[i] == 'u':
            cnt += 1
    print(cnt)