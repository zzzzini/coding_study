s = input()
for i in range(0,len(s),1):
    print(s[i],end='')
    if (i+1) % 10 == 0:
        print()