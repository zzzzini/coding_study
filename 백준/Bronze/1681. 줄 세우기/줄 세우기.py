n, l = map(int, input().split())
i = 1
cnt = 0

while True:
    if str(l) not in str(i):
        cnt += 1

    if cnt == n:
        break

    else:
        i += 1

print(i)