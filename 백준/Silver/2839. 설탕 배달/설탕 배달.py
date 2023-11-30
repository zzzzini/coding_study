n = int(input())
five = int(n/5)
three = 0
n %= 5
while five >= 0:
    if n % 3 == 0:
        three = n//3
        n = n % 3
        break
    five -= 1
    n += 5
print((n == 0) and (five + three) or -1)