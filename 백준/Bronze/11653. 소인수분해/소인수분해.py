n = int(input())
k = 2
while n != 1:
    if n % k == 0:
        n = n // k
        print(k)
    else:
        k += 1