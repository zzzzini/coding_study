sum = 0
num = []
key1 = 0
key2 = 0
for i in range(0,9,1):
    n = int(input())
    num.append(n)
    sum += n
num = sorted(num)
for i in range(0,9,1):
    for j in range(0,9,1):
        temp = num[i] + num[j]
        if sum - temp == 100:
            key1 = i
            key2 = j
num.remove(num[key1])
num.remove(num[key2])
for i in range(0,7,1):
    print(num[i])