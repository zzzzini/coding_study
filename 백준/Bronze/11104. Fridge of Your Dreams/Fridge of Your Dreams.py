n = int(input())
for k in range(0, n, 1):
    a = input()
    num = 0
    for i in range(0, len(a), 1):
        adv = 1
        for j in range(0, len(a) - (1+i), 1):
            adv *= 2
        num += int(a[i]) * adv
    print(num)