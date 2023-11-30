n = int(input())
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print("*", end='')
    print()
for i in range(n+1,2*n,1):
    for j in range(2*n,i,-1):
        print("*", end='')
    print()