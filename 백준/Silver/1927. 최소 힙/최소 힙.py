import sys
import heapq
hq = []

n = int(input())
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(hq) != 0:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, num)