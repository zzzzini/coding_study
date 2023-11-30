n = int(input())
for i in range(0,n,1):
    t = int(input())
    num = list(map(int,input().split()))
    print(2*(max(num)-min(num)))