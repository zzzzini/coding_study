n = int(input())
for i in range(n):
    num, loc = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = [k for k in range(num)]
    cnt = 0
    temp = 101

    while True:

        if imp[0] != max(imp):
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))

        else:
            imp.pop(0)
            temp = idx.pop(0)
            cnt += 1

        if temp == loc:
            break

    print(cnt)