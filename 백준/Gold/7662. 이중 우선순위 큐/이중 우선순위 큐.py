import sys
import heapq

for T in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    visited = [False] * k
    plus, minus = [], []
    for i in range(k):
        task, number = sys.stdin.readline().split()
        number = int(number)

        if task == 'I':
            heapq.heappush(plus, (number, i))
            heapq.heappush(minus, (-number, i))
            visited[i] = True
        elif number == 1:
            while minus and not visited[minus[0][1]]:
                heapq.heappop(minus)
            if minus:
                visited[minus[0][1]] = False
                heapq.heappop(minus)
        else:
            while plus and not visited[plus[0][1]]:
                heapq.heappop(plus)
            if plus:
                visited[plus[0][1]] = False
                heapq.heappop(plus)
    while plus and not visited[plus[0][1]]:
        heapq.heappop(plus)
    while minus and not visited[minus[0][1]]:
        heapq.heappop(minus)
    print(-minus[0][0], plus[0][0]) if plus and minus else print("EMPTY")