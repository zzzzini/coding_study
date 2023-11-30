a, b = map(int,input().split())
a = str(a)
b = str(b)
suma = 0
sumb = 0
for i in range(0,len(a),1):
    suma += int(a[i])
for i in range(0,len(b),1):
    sumb += suma * int(b[i])
print(sumb)