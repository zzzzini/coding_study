scene = 0
while True:
    scene += 1
    cnt = 0
    stu = []
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        stu.append(list(input().split()))

    print(f'Group {scene}')

    for i in range(n):
        temp = ''
        for j in range(1, n, 1):
            if stu[i][j] == 'N':
                diff = (i-j) if i>=j else (i-j+n)
                cnt += 1
                temp += f'{stu[diff][0]} was nasty about {stu[i][0]} '
        if temp != '':
            print(temp)

    if cnt == 0:
        print("Nobody was nasty")
    
    print()