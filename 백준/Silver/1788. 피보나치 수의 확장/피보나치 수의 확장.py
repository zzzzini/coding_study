n = int(input())
if n > 0:
    li = [0, 1]
    for i in range(2,n+1):
        li.append((li[i-2] + li[i-1]) % 1000000000)
elif n < 0:
    li = [1, 0]
    for i in range(2,abs(n)+2):
        temp = (li[i-2] - li[i-1])
        if temp >= 0:
            li.append((li[i-2] - li[i-1]) % 1000000000)
        else:
            li.append((li[i-2] - li[i-1]) % -1000000000)
else:
    li = [0]
    print(0)
    print(0)

if li[-1] < 0:
    print(-1)
    print(abs(li[-1]))
elif li[-1] > 0:
    print(1)
    print(abs(li[-1]))