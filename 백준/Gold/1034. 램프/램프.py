n, m = tuple(map(int, input().split()))
lst = []
for _ in range(n):
    lst.append(input())

k = int(input())
max_cnt = 0

for col in range(0,n,1):
    zero_count = 0
    for num in lst[col]:
        if num == '0':
            zero_count += 1

    col_light_cnt = 0
    if zero_count <= k and zero_count % 2 == k % 2:
        for col2 in range(n):
            if lst[col] == lst[col2]:
                col_light_cnt += 1

    max_cnt = max(max_cnt, col_light_cnt)

print(max_cnt)