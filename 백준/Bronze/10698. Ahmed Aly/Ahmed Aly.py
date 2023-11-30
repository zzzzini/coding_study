t = int(input())
for i in range(0,t,1):
    X, o, Y, e, Z = input().split()
    x, y, z = int(X), int(Y), int(Z)
    if o == '+':
        if x + y == z:
            s = "YES"
        else:
            s = "NO"
    elif o == '-':
        if x - y == z:
            s = "YES"
        else:
            s = "NO"
    print("Case", i+1, end='')
    print(":", s)