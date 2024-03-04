import sys
from collections import deque
li = deque()
for i in range(int(input())):
    s = sys.stdin.readline()
    if s[:3] == 'all':
        cmd = 'all'
    elif s[:5] == 'empty':
        cmd = 'empty'
    else:
        cmd, num = s.split()

    if cmd == "add":
        if int(num) not in li:
            li.append(int(num))
    elif cmd == "remove":
        if int(num) in li:
            li.remove(int(num))
    elif cmd == "check":
        print(1) if int(num) in li else print(0)
    elif cmd == "toggle":
        if int(num) in li:
            li.remove(int(num))
        else:
            li.append(int(num))
    elif cmd == "all":
        li = deque(k+1 for k in range(20))
    elif cmd == "empty":
        li = deque()