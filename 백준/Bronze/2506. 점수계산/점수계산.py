n = int(input())
lst = list(map(int, input().split()))
cnt = 1
sum = 0
if lst[0] == 1:
    sum += cnt
for i in range(1,n,1):
    if lst[i] == 1 and lst[i-1] == 1:
        cnt += 1
        sum += cnt
    elif lst[i] == 1 and lst[i-1] != 1:
        cnt = 1
        sum += cnt
print(sum)