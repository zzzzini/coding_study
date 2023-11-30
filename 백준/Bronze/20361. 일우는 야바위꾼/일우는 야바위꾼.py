n, x, k = map(int,input().split())
li = [0] * n
li[x-1] = 1
for i in range(0,k,1):
    one, two = map(int,input().split())
    li[one-1], li[two-1] = li[two-1], li[one-1]

for i in range(0,n,1):
    if li[i] == 1:
        print(i+1)