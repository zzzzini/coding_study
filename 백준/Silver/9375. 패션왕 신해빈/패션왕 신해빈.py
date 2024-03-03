for i in range(int(input())):
    dict = {}
    for j in range(int(input())):
        cloth, kind = input().split()
        if kind in dict.keys():
            dict[kind].append(cloth)
        else:
            dict[kind] = [cloth]
    count = 1
    key = list(dict.keys())
    for item in key:
        count *= (len(dict[item]) + 1)
    print(count - 1)