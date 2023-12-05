x,y,w,h = map(int, input().split())
xmin = 0
ymin = 0
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