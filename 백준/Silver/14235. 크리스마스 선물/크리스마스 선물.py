import heapq
heap = []

n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    num = a[0]
    present = a[1:]
    for item in present:
        heapq.heappush(heap, -item)

    if num == 0:
        if len(heap) != 0:
            print(-heapq.heappop(heap))
        else:
            print(-1)