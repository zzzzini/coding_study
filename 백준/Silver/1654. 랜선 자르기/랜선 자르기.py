k, n = map(int, input().split())
had = []
for i in range(k):
    had.append(int(input()))
left = 1
right = max(had)

while left <= right:
    mid = (left + right) // 2
    cnt = sum([k // mid for k in had])
    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)