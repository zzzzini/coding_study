n = int(input())
for i in range(0,n,1):
    a = int(input())
    t = 1
    sum = 0
    while t <= a:
        sum += t
        t += 2
    print(sum)