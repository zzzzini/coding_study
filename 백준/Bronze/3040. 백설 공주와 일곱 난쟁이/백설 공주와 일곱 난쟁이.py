sum = 0
num = []
key1 = 0
key2 = 0
for i in range(0,9,1):
    num.append(int(input()))
    sum += num[i]
diff = sum - 100
for i in range(0,8,1):
    for j in range(i+1,9,1):
        if num[i] + num[j] == diff:
            key1 = i
            key2 = j
num.remove(num[key1])
num.remove(num[key2-1])
for i in range(0,7,1):
    print(num[i])