n = int(input())
max = 0
for i in range(0,n,1):
    num = list(map(int, input().split()))
    cnt = 0
    for j in range(0,2,1):
        for k in range(j+1,3,1):
            if num[j] > num[k]:
                num[j], num[k] = num[k], num[j]

    for j in range(0,2,1):
        for k in range(j+1,3,1):
            if num[j] == num[k]:
                same = num[j]
                cnt += 1
    if cnt >= 2:
        money = (10000 + num[j] * 1000)
    elif cnt == 1:
        money = (1000 + num[j] * 100)
    else:
        money = (100 * num[2])
    if max < money:
        max = money
print(max)