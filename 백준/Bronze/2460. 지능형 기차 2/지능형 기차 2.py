sum = 0
max = 0
for i in range(0,10,1):
    a, b = map(int,(input().split()))
    sum -= a
    sum += b
    if sum > max:
        max = sum
print(max)