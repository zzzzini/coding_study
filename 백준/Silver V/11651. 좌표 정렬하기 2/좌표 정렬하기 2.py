n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

li.sort(key = lambda x:(x[1],x[0]))

for item in li:
    print(item[0], item[1])