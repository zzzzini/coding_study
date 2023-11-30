a = int(input())
b = int(input())
c = int(input())
num = list(str(a*b*c))
cnt = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,10,1):
    for j in range(1,len(num)+1,1):
        if int(num[j-1]) == i:
            cnt[i] += 1
    print(cnt[i])