n, k = map(int, input().split())
coin = []
cnt = 0
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
for item in coin:
    c, k = divmod(k, item)
    cnt += c
print(cnt)