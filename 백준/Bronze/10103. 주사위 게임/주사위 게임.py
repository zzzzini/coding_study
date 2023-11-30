n = int(input())
c = 100
s = 100
for i in range(0,n,1):
    num1, num2 = map(int, input().split())
    if num1 > num2:
        s -= num1
    elif num1 < num2:
        c -= num2
print(c)
print(s)