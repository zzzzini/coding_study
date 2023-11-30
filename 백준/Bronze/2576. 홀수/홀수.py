sum = 0
min = 100
for i in range(0,7,1):
    n = int(input())
    if n % 2 != 0:
        sum += n
        if n < min:
            min = n
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)