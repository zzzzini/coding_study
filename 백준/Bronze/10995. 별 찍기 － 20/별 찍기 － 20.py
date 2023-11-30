n = int(input())
cnt = 1
for i in range(0,n,1):
    if cnt > 0:
        for j in range(0,n,1):
            print("*"+" ", end='')
        cnt *= -1
    else:
        for j in range(0,n,1):
            print(" "+"*", end='')
        cnt *= -1
    print()