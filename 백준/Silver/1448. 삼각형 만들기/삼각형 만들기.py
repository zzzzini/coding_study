import sys
n = int(input())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))

li.sort(reverse = True)
len = -1

for i in range(n-2):
    if li[i+1] + li[i+2] > li[i]:
        len = max(len, li[i] + li[i+1] + li[i+2])
        break

print(len)