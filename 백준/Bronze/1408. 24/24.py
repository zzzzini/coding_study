h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))
if s2 > s1:
    s = s2 - s1
elif s2 == s1:
    s = 0
else:
    m2 -= 1
    s = s2 + 60 - s1

if m2 > m1:
    m = m2 - m1
elif m2 == m1:
    m = 0
else:
    h2 -= 1
    m = m2 + 60 - m1

if h2 > h1:
    h = h2 - h1
elif h2 == h1:
    h = 0
else:
    h = h2 + 24 - h1

time = [str(h), str(m), str(s)]
for i in range(len(time)):
    if len(time[i]) != 2:
        time[i] = "0" + time[i]

print(time[0]+":"+time[1]+":"+time[2])