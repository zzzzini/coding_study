s = input()
search = input()

cnt = 0
while True:
    if search in s:
        start = s.find(search)
        s = s[start+len(search):]
        cnt += 1
    else:
        break
print(cnt)