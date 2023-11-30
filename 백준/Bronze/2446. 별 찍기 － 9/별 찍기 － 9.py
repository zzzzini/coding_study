n = int(input())
for i in range(n,0,-1):
    for j in range(0,n-i,1):
        print(" ", end='')
    for j in range(1,2*i,1):
        print("*", end='')
    print()
for i in range(2,n+1,1):
    for j in range(0,n-i,1):
        print(" ", end='')
    for j in range(1,2*i,1):
        print("*", end='')
    print()