n, m = map(int, input().split())
state = []
cntr = 0
for i in range(n):
    t = input()
    state.append(t)
    if 'X' not in t:
        cntr += 1

cntc = 0
for j in range(m):
    temp = 0
    for i in range(n):
        if state[i][j] == 'X':
            temp += 1

    if temp == 0:
        cntc += 1

print(max(cntr, cntc))