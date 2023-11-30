n = int(input())
while True:
    a = int(input())
    if a == 0:
        break
    else:
        if a % n == 0:
            print(a,"is a multiple of",n,end='')
            print('.')
        else:
            print(a, "is NOT a multiple of", n, end='')
            print('.')