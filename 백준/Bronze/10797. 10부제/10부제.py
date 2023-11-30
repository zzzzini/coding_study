n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in range(0,len(lst),1):
    if lst[i] == n:
        cnt += 1
print(cnt)