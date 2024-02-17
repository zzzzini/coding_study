n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

if len(li) == 1:
    print(0)
else:
    dasom = li[0]
    original_dasom = dasom
    other = li[1:]
    while True:
        if dasom > max(other):
            break

        other[other.index(max(other))] -= 1
        dasom += 1
        
    print(dasom - original_dasom)