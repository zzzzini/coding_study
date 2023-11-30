n = int(input())
num = list(map(int,input().split()))
sosu = 0
for i in range(0,len(num),1):
    number = 0
    for k in range(1,num[i]+1,1):
        if num[i] % k == 0:
            number += 1
    if number == 2:
        sosu += 1
print(sosu)