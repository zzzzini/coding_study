s = input()
v = ['a','i','e','o','u']
cnt = 0
for i in range(0,len(s),1):
    if s[i] in v:
        cnt += 1
print(cnt)