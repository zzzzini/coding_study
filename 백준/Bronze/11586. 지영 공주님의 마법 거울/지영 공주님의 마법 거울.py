t = int(input())
s = []
for i in range(0,t,1):
    s.append(input())
status = int(input())
if status == 1:
    for i in range(0,t,1):
        for j in range(0,len(s[i]),1):
            print(s[i][j],end='')
        print()
elif status == 2:
    for i in range(0,t,1):
        for j in range(0,len(s[i]),1):
            print(s[i][len(s[i])-(j+1)],end='')
        print()
elif status == 3:
    for i in range(0,t,1):
        for j in range(0,len(s[i]),1):
            print(s[len(s)-(i+1)][j],end='')
        print()