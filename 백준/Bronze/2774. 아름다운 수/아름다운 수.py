n = int(input())
for i in range(0,n,1):
    num = input()
    find = []
    counter = 0
    for j in range(0,len(num),1):
        if num[j] not in find:
            find.append(num[j])
            counter += 1
    print(counter)