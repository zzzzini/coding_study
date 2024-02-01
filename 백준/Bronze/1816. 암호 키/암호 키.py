import math

def prime(num):
    flag = 1
    for i in range(2, 1000000, 1):
        if num % i == 0:
            flag = 0
            break
        else:
            continue

    return flag


n = int(input())
for i in range(n):
    num = int(input())

    if prime(num):
        print("YES")
    else:
        print("NO")