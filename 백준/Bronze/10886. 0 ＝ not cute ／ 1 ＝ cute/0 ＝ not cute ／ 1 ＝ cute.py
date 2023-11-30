n = int(input())
cnt1 = 0
cnt0 = 0
for i in range(0,n,1):
    a = int(input())
    if a == 1:
        cnt1 += 1
    elif a == 0:
        cnt0 += 1
if cnt1 > cnt0:
    print("Junhee is cute!")
elif cnt1 < cnt0:
    print("Junhee is not cute!")