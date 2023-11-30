n = int(input())

if n <= 10:
    print(n)
else:
    lst = list(range(0,10))
    cnt = 10
    t = True
    k = 0
    while t == True:
        lst2 = []
        for i in range(0, 10,1):
            for item in lst:
                if item == 9876543210:
                    k = 3
                    t = False
                if int(str(item)[0]) < i:
                    lst2.append( int(str(i) + str(item)))
                    cnt += 1
                    if cnt - 1 == n:
                        print(lst2[-1])
                        t = False
                else:
                    break
        if k == 3:
            print(-1)
        lst = lst2