r, l, a = map(int,input().split())
if r > l:
    r, l = l, r
while r < l and a != 0:
    a -= 1
    r += 1
if r == l:
    r += a//2
    l += a//2
diff = l - r
print(r+l-diff)