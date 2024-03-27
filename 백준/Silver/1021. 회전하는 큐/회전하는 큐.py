from collections import deque

n, m = map(int, input().split())
idx = list(map(int, input().split()))
dq = deque(k+1 for k in range(n))
cnt = 0
for item in idx:

    if dq[0] == item:
        dq.popleft()

    else:
        if dq.index(item) <= abs(dq.index(item) - len(dq)):
            while True:
                if dq[0] == item:
                    dq.popleft()
                    break
                dq.append(dq.popleft())
                cnt += 1
        else:
            while True:
                if dq[0] == item:
                    dq.popleft()
                    break
                dq.appendleft(dq.pop())
                cnt += 1
print(cnt)