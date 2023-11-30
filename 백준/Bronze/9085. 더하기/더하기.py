n = int(input())
for i in range(0,n,1):
    c = int(input())
    sum = 0
    lst = list(map(int, input().split()))
    for j in range(0,c,1):
        sum += lst[j]
    print(sum)