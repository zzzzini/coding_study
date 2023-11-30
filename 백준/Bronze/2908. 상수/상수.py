a, b = input().split()
new1 = ""
new2 = ""
for i in range(2,-1,-1):
    new1 += a[i]
    new2 += b[i]
if int(new1) > int(new2):
    print(int(new1))
else:
    print(int(new2))