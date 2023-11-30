case = int(input())
for i in range(0, case, 1):
    num, ch = input().split()
    n = int(num)
    for j in range(0, n, 1):
        print(ch, end='')
    print()