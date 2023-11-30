num = []
for i in range(0,9,1):
    num.append(list(map(int,input().split())))
xkey = 0
ykey = 0
max = -1
for i in range(0,9,1):
    for j in range(0,9,1):
        if num[i][j] > max:
            max = num[i][j]
            xkey = i
            ykey = j

print(max)
print(xkey+1, ykey+1)