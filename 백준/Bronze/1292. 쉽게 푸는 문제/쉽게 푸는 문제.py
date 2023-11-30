a, b = map(int,input().split())
num = []
for i in range(1,b+1,1):
    t = 0
    while i != t:
        num.append(i)
        t += 1
print(sum(num[a-1:b]))