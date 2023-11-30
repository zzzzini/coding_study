n = int(input())
ball = "1"
for i in range(0,n,1):
    a, b = input().split()
    if a == ball:
        ball = b
    elif b == ball:
        ball = a
if int(ball) >= 1:
    print(ball)
else:
    print(-1)