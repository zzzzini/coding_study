import sys
import heapq
plus = []
minus = []
for i in range(int(input())):
    number = int(sys.stdin.readline())

    if number > 0:
        heapq.heappush(plus, number)
    elif number < 0:
        heapq.heappush(minus, -number)
    else:
        if plus and minus:
            if abs(plus[0]) >= abs(minus[0]):
                print(-heapq.heappop(minus))
            else:
                print(heapq.heappop(plus))
        elif plus and not minus:
            print(heapq.heappop(plus))
        elif minus:
            print(-heapq.heappop(minus))
        else:
            print(0)