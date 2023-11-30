a, b = input().split()
maxa = []
maxb = []
mina = []
minb = []

for i in range(0,len(a),1):
    if a[i] == "5":
        maxa.append("6")
        mina.append("5")
    elif a[i] == "6":
        maxa.append("6")
        mina.append("5")
    else:
        maxa.append(a[i])
        mina.append(a[i])

for i in range(0,len(b),1):
    if b[i] == "5":
        maxb.append("6")
        minb.append("5")
    elif b[i] == "6":
        maxb.append("6")
        minb.append("5")
    else:
        maxb.append(b[i])
        minb.append(b[i])

s1 = ""
s2 = ""
s3 = ""
s4 = ""
for item in mina:
    s1 += str(item)
for item in minb:
    s2 += str(item)
for item in maxa:
    s3 += str(item)
for item in maxb:
    s4 += str(item)
min = int(s1) + int(s2)
max = int(s3) + int(s4)
print(min, max)