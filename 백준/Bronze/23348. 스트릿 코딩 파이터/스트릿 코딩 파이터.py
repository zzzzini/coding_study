a, b, c = map(int,input().split())
n = int(input())
score = 0
for i in range(0,n,1):
    sum = 0
    for j in range(0,3,1):
        o, n, p = map(int,input().split())
        sum += (a*o + b*n + c*p)
    if sum > score:
        score = sum
print(score)