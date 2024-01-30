import sys
n = int(input())
word = [['' for i in range(50)] for j in range(50)]
for i in range(n):
    s = sys.stdin.readline().strip()
    word[len(s)-1].append(s)
for items in word:
    temp = set(items)
    items = list(temp)
    items.sort()
    for item in items:
        if item != '':
            print(item)