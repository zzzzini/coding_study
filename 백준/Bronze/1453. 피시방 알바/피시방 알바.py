n = int(input())
num = []
for i in range(1,101,1):
    num.append(i)
numbers = list(map(int,input().split()))
counter = 0
for i in range(0,n,1):
    if numbers[i] in num:
        num.remove(numbers[i])
    else:
        counter += 1
print(counter)