import sys
n = int(input())
word = [[] for i in range(50)]
for i in range(n):
    s = sys.stdin.readline().strip()
    word[len(s)-1].append(s)
for items in word:
    if items != []:
        temp = list(set(items))
        temp.sort()
        for item in temp:
            print(item)