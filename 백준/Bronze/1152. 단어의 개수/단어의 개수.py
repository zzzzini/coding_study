s = input().split(" ")
cnt = 0
for i in range(0,len(s),1):
    if s[i] != "":
        cnt += 1
print(cnt)