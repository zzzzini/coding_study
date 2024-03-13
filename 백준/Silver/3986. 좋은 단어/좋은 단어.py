from collections import deque
n = int(input())
cnt = 0
for i in range(n):
    word = input()
    li = deque()
    for item in word:
        if item not in li:
            li.append(item)
        else:
            if item == li[-1]:
                li.pop()
            else:
                li.append(item)
    if len(li) == 0:
        cnt += 1
print(cnt)