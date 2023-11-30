n = int(input())
for i in range(0,n,1):
    A, s = input().split()
    a = int(A)
    for j in range(0,a-1,1):
        print(s[j], end='')
    for j in range(a,len(s),1):
        print(s[j], end='')
    print()