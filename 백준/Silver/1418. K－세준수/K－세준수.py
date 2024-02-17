import math
def sosu(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
            break
    else:
        return True

def soinsu(num):
    li = []
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            if sosu(i):
                li.append(i)
            if sosu(num//i):
                li.append(num//i)

    if len(li) == 0:
        li.append(num)
    return li

n = int(input())
k = int(input())
cnt = 0

for i in range(1, n+1):
    if max(soinsu(i)) <= k:
        cnt += 1
print(cnt)