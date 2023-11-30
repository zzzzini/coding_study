n = int(input())
num1 = n // 300
num2 = (n % 300) // 60
num3 = ((n % 300) % 60) // 10
if ((n % 300) % 60) % 10 != 0:
    print(-1)
else:
    print(num1, num2, num3)