numbers = list(map(int, input().split()))
m = min(numbers)

while True:
    cnt = 0
    for item in numbers:
        if m % item == 0:
            cnt += 1
    if cnt >= 3:
        break
    m += 1

print(m)