n = int(input())
li = list(map(int,input().split()))
li.sort()
if n == 1:
    print(li[0] ** 2)
else:
    print(li[0] * li[n-1])