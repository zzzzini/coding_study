from itertools import product

for i in range(int(input())):
    n = int(input())
    flag = False
    li = [k for k in range(1,n+1)]
    for i in range(1,len(li)):
        li[i] += li[i-1]
        if li[i] >= n:
            li = li[:i+1]
            break

    for item in product(li, repeat=3):
        if sum(item) == n:
            flag = True
            break

    if flag:
        print(1)
    else:
        print(0)