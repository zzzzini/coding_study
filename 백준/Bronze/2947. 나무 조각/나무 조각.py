n = list(map(int, input().split()))
while n != sorted(n):
    for i in range(0,4,1):
        if n[i] > n[i+1]:
            n[i], n[i+1] = n[i+1], n[i]
            for k in range(0,5,1):
                print(n[k], end=' ')
            print()