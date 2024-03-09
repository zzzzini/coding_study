import sys
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
stack = [nums[0]]
for i in range(1,len(nums)):
    stack.append(stack[i-1] + nums[i])
for k in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(stack[j-1])
    else:
        print(stack[j-1] - stack[i-2])