n = int(input())
for i in range(0,n,1):
    x, y = map(int, input().split())
    d = y - x
    max = int(d ** 0.5)
    test = max ** 2
    counter = 0
    if d == test:
        counter = max * 2 - 1
    elif d <= test + max:
        counter = max * 2
    elif d > test + max:
        counter = max * 2 + 1
    elif d < 4:
        counter = d
    print(counter)