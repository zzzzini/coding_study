ab, ac, bc= map(int,input().strip().split())
b=(ab - ac + bc) / 2
a = ab - b
c = ac - a

if a<1 or b<1 or c<1:
    print(-1)
else:
    print(1)

if a >= 1 and b >= 1 and c >= 1:
    print(a,b,c)