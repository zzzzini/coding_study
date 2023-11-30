r, c, zr, zc = map(int,input().split())
s = []
for i in range(0,r,1):
    s.append(input())
for i in range(0,r,1):
    for k in range(0,zr,1):
        for j in range(0,c,1):
            for l in range(0,zc,1):
                print(s[i][j], end='')
        print()