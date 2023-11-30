n, l = map(int,input().split())
h = list(map(int,input().split()))
for i in range(0,n,1):
    a = []
    for j in range(0,len(h),1):
        if l >= h[j]:
            l += 1
            a.append(h[j])
    for j in range(0,len(a),1):
        if a[j] in h:
            h.remove(a[j])
print(l)