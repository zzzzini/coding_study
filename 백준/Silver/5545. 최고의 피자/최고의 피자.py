n = int(input())
a, b = map(int, input().split())
c = int(input())
d = []
for i in range(n):
    d.append(int(input()))

d.sort(reverse=True)
cal = c
best = cal // a
i = 1

for item in d:
    cal += item
    best = max(best, cal//(a+b*i))
    i += 1

print(best)