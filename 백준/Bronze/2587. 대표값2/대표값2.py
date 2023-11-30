num = []
for i in range(0,5,1):
    num.append(int(input()))
num.sort()
print(sum(num) // 5, num[2])