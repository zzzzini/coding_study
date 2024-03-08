import sys
n = int(input())
cust = []
money1 = 0
money2 = 0
for i in range(n):
    cust.append(int(sys.stdin.readline()))
custwo = sorted(cust)
cust.sort(reverse=True)
idx = 1
for item in cust:
    tip = item-(idx-1)
    if tip <= 0:
        continue
    else:
        money1 += tip
        idx += 1

idx = 1
for item in custwo:
    tip = item-(idx-1)
    if tip <= 0:
        continue
    else:
        money2 += tip
        idx += 1
print(max(money1, money2))