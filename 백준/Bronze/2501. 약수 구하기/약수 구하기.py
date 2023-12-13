n, k = map(int, input().split())
a = []
for i in range(1,n//2,1):
    if n % i == 0 and i not in a:
        a.append(i)
        if i != n//i:
            a.append(n//i)
a.sort()
if len(a) < k:
    print(0)
else:
    print(a[k-1])