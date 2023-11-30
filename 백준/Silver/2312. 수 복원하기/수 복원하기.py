import math

def sosu(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

n = int(input())
for i in range(0,n,1):
    num = int(input())
    numbers = []
    counter = []
    for j in range(1,num+1,1):
        count = 0
        if sosu(j):
            while True:
                if num % j != 0:
                    break
                else:
                    num /= j
                    count += 1
        if count != 0:
            numbers.append(j)
            counter.append(count)
    for i in range(0,len(numbers),1):
        print(numbers[i], counter[i])