n = int(input())
l = 2
for i in range(1,n+1,1):
    p = 1
    for j in range(1,i,1):
        p *= 2
    l += p
print(l*l)