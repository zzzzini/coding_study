n = int(input())
li = []

for i in range(n):
    li.append(input())

answer = list(li[0])

for i in range(1, len(li), 1):
    for j in range(0, len(li[0]), 1):
        if li[0][j] != li[i][j]:
            answer[j] = '?'

for item in answer:
    print(item,end='')