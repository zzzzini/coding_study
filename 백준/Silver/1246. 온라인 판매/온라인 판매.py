n, m = map(int, input().split())
p = []
profit = []

for i in range(m):
    p.append(int(input()))

for item in p:
    minimum = item
    customers = [k for k in p if k >= item]
    if len(customers) > n:
        profit.append([item, item * n])
    else:
        profit.append([item, item * len(customers)])

profit = [k for k in profit if k[1] == max([k[1] for k in profit])]
profit.sort()
print(profit[0][0], profit[0][1])