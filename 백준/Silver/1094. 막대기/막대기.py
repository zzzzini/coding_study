x = int(input())
length = [32, 16, 8, 4, 2, 1, 1]
sums = []
for i in length :
    if (i <= x) & ((sum(sums) + i) <= x) :
        sums.append(i)
if x == 64 :
    print(1)
else :
    print(len(sums))