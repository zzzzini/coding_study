n = int(input())
li = []
lcnt = 0
rcnt = 0
for i in range(n):
    t = int(input())
    if i == 0:
        lcnt += 1
        max = t
    else:
        if t > max:
            lcnt += 1
            max = t
    li.append(t)

for i in range(n-1,-1,-1):
    if i == n-1:
        rcnt += 1
        max = li[i]
    else:
        if li[i] > max:
            rcnt += 1
            max = li[i]

print(lcnt)
print(rcnt)