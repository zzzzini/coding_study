n = int(input())
num = []
diff = []
div = []
cnt = 0
for i in range(0,n,1):
    num.append(int(input()))
for i in range(1,len(num),1):
    div.append(num[i]//num[i-1])
    diff.append(num[i]-num[i-1])
for i in range(1,len(diff),1):
    if diff[i] != diff[0]:
        cnt += 1
if cnt >= 1:
    print(num[n-1]*div[0])
else:
    print(num[n-1]+diff[0])