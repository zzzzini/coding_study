n = int(input())
for i in range(0,n,1):
    NUM, s = input().split()
    num = int(NUM)
    for j in range(0,len(s),1):
        for k in range(0,num,1):
            print(s[j],end='')
    print()