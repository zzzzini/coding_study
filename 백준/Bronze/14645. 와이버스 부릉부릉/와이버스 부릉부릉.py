inbus = 0
n, k = map(int,input().split())
inbus += k
for i in range(0,n,1):
    inside, outside = map(int,input().split())
    inbus += inside
    inbus -= outside
lastman = inbus
inbus -= lastman
print("비와이")