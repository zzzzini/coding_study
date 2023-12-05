import sys
n = int(sys.stdin.readline())
ans = [0] * 10001
for i in range(n):
    ans[int(sys.stdin.readline())] += 1

for i in range(len(ans)):
    if ans[i] != 0:
        for j in range(ans[i]):
            print(i)