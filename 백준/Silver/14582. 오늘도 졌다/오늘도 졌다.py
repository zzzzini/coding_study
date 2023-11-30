a = list(map(int,input().split()))
b = list(map(int,input().split()))
fact = 0
sum1 = 0
sum2 = 0
for i in range(0,9,1):
    sum1 += a[i]
    if sum1 > sum2:
        fact += 1
    sum2 += b[i]
if fact >=1 and sum(a) < sum(b):
    print("Yes")
else:
    print("No")