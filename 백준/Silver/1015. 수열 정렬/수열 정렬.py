n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
p = []
for i in range(len(a)):
    temp = a[:i]
    if b.index(a[i]) in p:
        p.append(b.index(a[i]) + temp.count(a[i]))
    else:
        p.append(b.index(a[i]))
for item in p:
    print(item, end=' ')