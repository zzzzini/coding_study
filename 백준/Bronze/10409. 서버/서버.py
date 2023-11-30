a, b = map(int,input().split())
li = list(map(int,input().split()))
cnt = 0
for i in range(0,a,1):
    b -= li[i]
    if b >= 0:
        cnt += 1
print(cnt)