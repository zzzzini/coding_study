n = int(input())
for i in range(0,n,1):
    r, e, c = map(int, input().split())
    if r > e - c:
        print("do not advertise")
    elif r == e - c:
        print("does not matter")
    else:
        print("advertise")