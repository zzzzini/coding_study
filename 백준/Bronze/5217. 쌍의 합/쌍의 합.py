n = int(input())
for i in range(0,n,1):
    t = 1
    number = int(input())
    print("Pairs for", number, end='')
    print(": ", end='')
    while True:
        n = number - t
        if t >= n:
            break
        else:
            if t == 1:
                print(t, n, end='')
            else:
                print(",", t, n, end='')
            t += 1
    print()