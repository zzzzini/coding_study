a,b,c = map(int,input().split())
s = []
t = []
for i in range(1,a+1,1):
    for j in range(1,b+1,1):
        for k in range(1,c+1,1):
            s.append(i+j+k)
            if i+j+k not in t:
                t.append(i+j+k)
s.sort()
t.sort()
count = [0] * len(t)
for i in range(0,len(t),1):
    for j in range(0,len(s),1):
        if t[i] == s[j]:
            count[i] += 1
max = 0
key = 0
for i in range(0,len(count),1):
    if count[i] > max:
        max = count[i]
        key = i
print(t[key])