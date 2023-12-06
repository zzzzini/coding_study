import sys

input = sys.stdin.readline
n = int(input())
l = list()
for i in range(n):
    command = input().rstrip().split()
    if command[0] == "push":
        l.append(command[1])
    elif command[0] == "pop":
        if len(l) == 0:
            print(-1)
        else:
            print(l.pop(0))
    elif command[0] == "size":
        print(len(l))
    elif command[0] == "empty":
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])
    elif command[0] == "back":
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])