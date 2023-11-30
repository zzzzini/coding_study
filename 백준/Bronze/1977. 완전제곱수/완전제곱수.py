import math
m = int(input())
n = int(input())
multi = []
min = n
sum = 0
for i in range(m, n+1, 1):
    if math.sqrt(i) == i//math.sqrt(i):
        multi.append(i)
        sum += i
        if i < min:
            min = i
if len(multi) != 0:
    print(sum)
    print(min)
else:
    print(-1)