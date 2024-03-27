n = int(input())
li = list(map(int, input().split()))
temp = sorted(set(li))
dict = {}
i = 0
for item in temp:
    dict[item] = i
    i += 1

for item in li:
    print(dict[item], end=' ')