n = int(input())
for i in range(0,n,1):
    s = input()
    t = s[0].upper()
    print(t,end='')
    for j in range(1,len(s),1):
        print(s[j],end='')
    print()