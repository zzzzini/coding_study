n = int(input())
p = list(map(int,input().split()))
p.sort()
for i in range(0,len(p)-1,1):
    p[i+1] += p[i]
print(sum(p))