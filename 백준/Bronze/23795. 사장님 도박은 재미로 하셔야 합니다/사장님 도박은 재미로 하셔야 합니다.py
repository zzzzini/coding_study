i = 1
sum = 0
while i < 2000:
    n = int(input())
    if n == -1:
        break
    else:
        sum += n
        i += 1
print(sum)