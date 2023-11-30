n = input()
num = 1
sum = 0
for i in range(0,len(n),1):
    for j in range(0,5,1):
        num *= int(n[i])
    sum += num
    num = 1
print(sum)