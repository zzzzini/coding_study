import sys
from queue import PriorityQueue
que = PriorityQueue()
n = int(input())
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if que.qsize() != 0:
            print(que.get())
        else:
            print(0)
    else:
        que.put(num)