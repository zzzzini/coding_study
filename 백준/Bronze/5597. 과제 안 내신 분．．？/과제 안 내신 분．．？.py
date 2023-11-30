a = []
for i in range(1,31,1):
    a.append(i)
b = []
for i in range(0,28,1):
    b.append(int(input()))
for i in range(0,28,1):
    if b[i] in a:
        a.remove(b[i])
a.sort()
for i in range(0,2,1):
    print(a[i])