scene = 0
while True:
    scene += 1
    stu = []
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        stu.append(input())

    apsu = []
    for i in range(2*n-1):
        a, b = input().split()
        apsu.append(a)

    unique = set(apsu)

    idx = 0
    for item in unique:
        if apsu.count(item) % 2 == 1:
            idx = item
            break

    print(scene, stu[int(idx)-1])