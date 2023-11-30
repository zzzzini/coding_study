n = int(input())
for i in range(0,n,1):
    l = list(map(int,input().split()))
    print("Scenario #",end='')
    print(i+1,end='')
    print(':')
    l.sort()
    if l[0] ** 2 + l[1] ** 2 == l[2] ** 2:
        print("yes")
    else:
        print("no")
    print()