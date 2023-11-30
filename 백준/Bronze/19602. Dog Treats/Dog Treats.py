num = []
sum = 0
for i in range(1,4,1):
    num.append(int(input()))
    sum += i * num[i-1]
if sum >= 10:
    print("happy")
else:
    print("sad")