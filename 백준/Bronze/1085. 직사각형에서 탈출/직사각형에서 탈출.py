X,Y,W,H = input().split()
x,y,w,h = int(X),int(Y),int(W),int(H)
xmin = w
ymin = h
if x < w-x:
    xmin = x
else:
    xmin = w-x
if y < h-y:
    ymin = y
else:
    ymin = h-y
if xmin < ymin:
    print(xmin)
else:
    print(ymin)