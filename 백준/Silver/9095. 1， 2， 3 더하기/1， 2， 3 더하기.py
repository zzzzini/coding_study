def func(n):
    li = [0 for k in range(n+1)]
    li[0] = 1

    for i in range(1, n+1):
        if i >= 1:
            li[i] += li[i-1]
        if i >= 2:
            li[i] += li[i-2]
        if i >= 3:
            li[i] += li[i-3]

    return(li[n])

for i in range(int(input())):
    print(func(int(input())))