n = int(input())
for i in range(0,n,1):
    s = int(input())
    csum = 0
    gsum = 0.0
    for j in range(0,s,1):
        C, G = input().split()
        c, g = int(C), float(G)
        csum += c
        gsum += g * c
    print(csum, f'{gsum/csum:.1f}')