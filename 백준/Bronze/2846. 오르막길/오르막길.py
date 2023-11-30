n = int(input())
stk = []
stack = 0
l = list(map(int,input().split()))
for i in range(1,n,1):
    if l[i] > l[i-1]:
        stack += l[i] - l[i-1]
    else:
        stk.append(stack)
        stack = 0
stk.append(stack)
stk.sort()
print(stk[len(stk)-1])