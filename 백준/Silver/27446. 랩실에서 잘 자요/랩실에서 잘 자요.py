n, m = map(int, input().split())
pages = list(map(int, input().split()))
paper = [k+1 for k in range(n)]
printing = [k for k in paper if k not in pages]

ink = 0
for i in range(len(printing)):
    if i == 0:
        ink += 7
    else:
        ink += min(7, (printing[i] - printing[i-1])*2)

print(ink)