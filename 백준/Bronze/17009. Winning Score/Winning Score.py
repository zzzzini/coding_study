a = 0
b = 0
for i in range(0,3,1):
    num = int(input())
    a += num * (3-i)
for j in range(0,3,1):
    num = int(input())
    b += num * (3-j)
if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("T")