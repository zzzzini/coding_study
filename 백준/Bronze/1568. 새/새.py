n = int(input())
t = 0
ad = 0
while True:
    ad += 1
    t += 1
    if n < ad:
        ad = 0
        t -= 1
    else:
        n -= ad
    if n == 0:
        break
print(t)