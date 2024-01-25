t = int(input())

for i in range(t):
    input()
    n, m = map(int, input().split())
    ps = sorted(list(map(int, input().split())))
    pb = sorted(list(map(int, input().split())))

    while True:
        if len(ps) == 0 or len(pb) == 0:
            break

        if ps[0] >= pb[0]:
            pb.remove(pb[0])
        else:
            ps.remove(ps[0])

    if len(ps) == 0:
        print('B')
    elif len(pb) == 0:
        print('S')
    else:
        print('C')