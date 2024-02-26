n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    li = list(map(int, input().split()))
    box = [m] * n
    k = 0
    for i in range(n):
        boxno = box[k]
        if li[i] > box[k]:
            box[k+1] -= li[i]
            k += 1
        else:
            box[k] -= li[i]

    print(len([k for k in box if k != m]))