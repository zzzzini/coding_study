n = int(input())
ori = list(input())
cnt = 0
for _ in range(n-1):
    tmp = ori[:]
    str = list(input())
    for _ in range(len(str)):
        a = str.pop(0)
        if a in tmp:
            tmp.remove(a)
        else:
            str.append(a)
    if len(tmp) == 1:
        if len(str) == 0 or len(str) == 1:
            cnt+=1
    elif len(tmp) == 0:
        if len(str) == 0 or len(str) == 1:
            cnt+=1
print(cnt)