y, m, d = map(int, input().split())
y1, m1, d1 = map(int, input().split())
if y == y1:
    print(0)
elif m < m1 or (m == m1 and d <= d1):
    print(y1 - y)
else:
    print(y1 - y - 1)
print(y1-y+1)
print(y1-y)