n = int(input())
count = 0
for i in range(0,n,1):
    s = input()
    no = 0
    for j in range(0,len(s)-1,1):
        for k in range(j+1,len(s),1):
            if s[j] == s[k]:
                if abs(k-j) != 1:
                    no += 1
                break
    if no == 0:
        count += 1
print(count)