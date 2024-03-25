n,m=map(int,input().split())
p=list(map(int,input().split()))
e=[k+1 for k in range(n)]
g,r=[k for k in e if k not in p],0
for i in range(len(g)):
    r += 7 if i == 0 else min(7, (g[i] - g[i-1])*2)
print(r)