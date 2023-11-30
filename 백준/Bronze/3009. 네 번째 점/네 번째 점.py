x = []
y = []
for i in range(0,3,1):
    X,Y = input().split()
    x.append(int(X))
    y.append(int(Y))
if x[0] == x[1]:
    x.append(x[2])
elif x[1] == x[2]:
    x.append(x[0])
elif x[2] == x[0]:
    x.append(x[1])
if y[0] == y[1]:
    y.append(y[2])
elif y[1] == y[2]:
    y.append(y[0])
elif y[2] == y[0]:
    y.append(y[1])
print(x[3], y[3])