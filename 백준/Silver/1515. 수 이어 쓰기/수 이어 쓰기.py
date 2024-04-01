n = list(input())
i = 1
while True:
    for num in str(i):
        if num == n[0]:
            n.pop(0)
            if len(n) == 0:
                print(i)
                exit()
    i += 1