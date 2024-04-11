n = int(input())
cnt = int(input())
current = 0
minimum = 1000000
maximum = 1000000

if cnt == 0:
    print(min(len(str(n)), abs(n-100)))
else:
    broken = list(input().split())
    if n == 100:
        print(0)
    else:
        while current <= 1000000:
            if all(num not in broken for num in str(current)) and current < n :
                minimum = current
            elif all(num not in broken for num in str(current)) and current == n:
                break
            elif all(num not in broken for num in str(current)) and current > n:
                maximum = current
                break
            current += 1

        if current == n:
            print(min(len(str(current)), abs(n-100)))
        else:
            print(min(len(str(minimum))+abs(n-minimum), len(str(maximum))+abs(maximum-n), abs(n-100)))