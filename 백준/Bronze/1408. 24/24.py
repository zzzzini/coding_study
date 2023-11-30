H1, M1, S1 = input().split(":")
H2, M2, S2 = input().split(":")
h1, m1, s1 = int(H1), int(M1), int(S1)
h2, m2, s2 = int(H2), int(M2), int(S2)
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

H, M, S = str(h), str(m), str(s)
if len(H) != 2:
    H = "0" + H
if len(M) != 2:
    M = "0" + M
if len(S) != 2:
    S = "0" + S

print(H+":"+M+":"+S)