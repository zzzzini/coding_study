n, k = map(int, input().split())
a = []
for i in range(1,n//2,1):
    if n % i == 0 and i not in a:
        a.append(i)
        if i != n//i:
            a.append(n//i)
for i in range(0,len(a)-1,1):
    for j in range(i+1,len(a),1):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
if len(a) < k:
    print(0)
else:
    print(a[k-1])