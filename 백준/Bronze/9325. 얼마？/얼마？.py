n = int(input())
for i in range(0,n,1):
    money = int(input())
    t = int(input())
    if t != 0:
        for j in range(0,t,1):
            a, b = map(int, input().split())
            money += a * b
    print(money)