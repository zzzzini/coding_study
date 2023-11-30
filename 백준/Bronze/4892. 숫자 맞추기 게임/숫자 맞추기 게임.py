t = 1
while True:
    n = int(input())
    original = 0
    status = "NULL"
    if n == 0:
        break
    n = n * 3
    if n % 2 == 0:
        status = "even"
        n = n // 2
        n = 3 * n
        n = n // 9
    else:
        status = "odd"
        n = (n + 1) // 2
        n = 3 * n
        n = n // 9
    print(t, end='')
    print(".", end=' ')
    print(status, n)
    t += 1