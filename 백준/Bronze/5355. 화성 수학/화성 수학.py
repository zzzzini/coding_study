num = int(input())
for i in range(0,num,1):
    no = list((input().split()))
    n = float(no[0])
    for j in range(1,len(no),1):
        if no[j] == "@":
            n *= 3
        elif no[j] == "%":
            n += 5
        elif no[j] == "#":
            n -= 7
    print(f'{n:.2f}')