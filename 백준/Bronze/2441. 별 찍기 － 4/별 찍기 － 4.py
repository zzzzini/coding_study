n = int(input())
for i in range(n, 0, -1):
    for j in range(n-i, 0, -1):
        print(" ", end='')
    for j in range(0, i, 1):
        print("*", end='')
    print()