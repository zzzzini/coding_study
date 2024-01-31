n = int(input())
i = 0
sum = 0

while True:
    i += 1
    if sum + i >= n:
        break
    sum += i

left = n - sum
hap = i+1
head = hap - left

if hap % 2:
    print("%d/%d" % (left, head))
else:
    print("%d/%d" % (head, left))