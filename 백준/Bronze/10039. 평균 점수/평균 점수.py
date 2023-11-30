sum = 0
for i in range(0,5,1):
    num = int(input())
    if num < 40:
        num = 40
    sum += num
print(sum//5)