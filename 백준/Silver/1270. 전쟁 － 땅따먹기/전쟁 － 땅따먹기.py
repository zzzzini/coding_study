n = int(input())
for i in range(n):
    li = list(map(int, input().split()))
    num = li[0]
    soldiers = li[1:]
    SYJKGW = True

    dict = {}

    for item in soldiers:
        if item not in dict.keys():
            dict[item] = 1
        else:
            dict[item] += 1

            if dict[item] > num / 2:
                SYJKGW = False
                target = item

    if SYJKGW:
        print("SYJKGW")
    else:
        print(target)