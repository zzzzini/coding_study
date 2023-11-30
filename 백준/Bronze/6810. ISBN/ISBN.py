sum = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3
cnt = 1
for i in range(0,3,1):
    n = int(input())
    if cnt % 2 == 0:
        sum += n * 3
    else:
        sum += n * 1
    cnt += 1
print("The 1-3-sum is", sum)