from collections import deque

for i in range(int(input())):
    task = input()
    n = int(input())
    li = input()
    flag = True
    if n > 0:
        li = deque(li[1:-1].split(","))
    else:
        li = deque()

    point = 0
    for item in task:
        if item == 'R':
            point = abs(1 - point)
        else:
            if len(li) == 0:
                flag = False
                break
            else:
                if point:
                    li.pop()
                else:
                    li.popleft()
    if flag:
        if point == 1:
            li = reversed(li)
        print('[', end='')
        print(','.join(list(li)), end='')
        print(']')
    else:
        print('error')