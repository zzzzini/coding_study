import sys
input = sys.stdin.readline
chess = []
for i in range(0,8,1):
    chess.append(input().strip())
counter = 0
for i in range(0,8,1):
    for j in range(0,8,1):
        if i % 2 == 0:
            if j % 2 == 0:
                if chess[i][j] == "F":
                    counter += 1
        else:
            if j % 2 == 1:
                if chess[i][j] == "F":
                    counter += 1
print(counter)