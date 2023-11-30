num = []
for i in range(0,10,1):
    num.append(int(input()))
num.sort()
counter = 0
max = 0
c = 0
key = 0
for i in range(1,10,1):
    if num[i] == num[i-1]:
        counter += 1
        c = i
        if max < counter:
            max = counter
            key = i
    else:
        counter = 0

print(sum(num) // 10, num[key])