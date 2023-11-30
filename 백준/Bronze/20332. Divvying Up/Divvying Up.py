n = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(0,n,1):
    sum += a[i]
if sum % 3 == 0:
    print("yes")
else:
    print("no")