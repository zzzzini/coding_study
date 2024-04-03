n = int(input())
li = [0,1,2]
if n < 3:
    pass
else:
    for i in range(3,n+1):
        li.append((li[i-2] + li[i-1]) % 10007)
print(li[n])