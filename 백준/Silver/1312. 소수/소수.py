a, b, n = map(int, input().split())
cnt = -1

while True:
    if cnt == n:
        break

    left, right = a // b, a % b
    right *= 10
    a = right

    cnt += 1

print(left)