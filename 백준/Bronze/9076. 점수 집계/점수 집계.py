n = int(input())
for i in range(0,n,1):
    l = list(map(int,input().split()))
    l.sort()
    sum = l[1] + l[2] + l[3]
    if l[3] - l[1] >= 4:
        print("KIN")
    else:
        print(sum)