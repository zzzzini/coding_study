str = input()
plus = str.split('-')
sums = []
for item in plus:
    sum = 0
    temp = item.split('+')
    for items in temp:
        sum += int(items)
    sums.append(sum)

minus = sums[0]
for i in range(1, len(sums)):
    minus -= sums[i]
print(minus)