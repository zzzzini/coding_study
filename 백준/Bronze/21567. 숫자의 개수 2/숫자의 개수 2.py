a = int(input())
b = int(input())
c = int(input())
s = str(a*b*c)
cnt = [0] * 10
for i in range(0,len(s),1):
    for j in range(0,10,1):
        if j == int(s[i]):
            cnt[j] += 1
for i in range(0,len(cnt),1):
    print(cnt[i])