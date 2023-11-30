a, b = map(int, input().split())
num = (a * b)
while b != 0:
    r = a % b
    a = b
    b = r
num = num // a
print(a)
print(num)