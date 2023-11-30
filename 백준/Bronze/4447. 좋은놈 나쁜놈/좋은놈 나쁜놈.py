n = int(input())
for i in range(0,n,1):
    cntg = 0
    cntb = 0
    s = input()
    t = s.lower()
    for j in range(0,len(t),1):
        if t[j] == 'g':
            cntg += 1
        elif t[j] == 'b':
            cntb += 1
    if cntg > cntb:
        print(s, "is GOOD")
    elif cntg == cntb:
        print(s, "is NEUTRAL")
    else:
        print(s, "is A BADDY")