import sys
input = sys.stdin.readline

n = int(input())

stack = [1]
k = 1
ans = []
flag = True

for i in range(n):

    num = int(input())

    while num >= k:
        stack.append(k)
        ans.append('+')
        k += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    else:
        flag = False
        break

if flag:
    for item in ans:
        print(item)
else:
    print('NO')