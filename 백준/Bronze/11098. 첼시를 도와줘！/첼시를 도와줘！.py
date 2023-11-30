n = int(input())
for i in range(0,n,1):
    p = int(input())
    max = 0
    index = "0"
    for j in range(0,p,1):
        COST, NAME = input().split()
        if int(COST) > max:
            max = int(COST)
            index = NAME
    print(index)