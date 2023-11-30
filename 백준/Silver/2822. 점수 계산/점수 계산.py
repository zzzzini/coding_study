num = []
temp = []
key = []
for i in range(0,8,1):
    num.append(int(input()))
    temp.append(num[i])
num.sort()
sum = 0
for i in range(3,8,1):
    sum += num[i]
    for j in range(0,8,1):
        if num[i] == temp[j]:
            key.append(j)
key.sort()
print(sum)
for i in range(0,5,1):
    print(key[i]+1, end=' ')