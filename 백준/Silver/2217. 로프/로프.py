import sys
from collections import deque

n = int(input())
dq = deque()
for i in range(n):
    dq.append(int(sys.stdin.readline()))

dq = deque(sorted(dq))

cnt = 0
maximum = 0

while True:
    if len(dq) == 0:
        break

    num = dq.pop()
    cnt += 1

    maximum = max(maximum, num*cnt)

print(maximum)