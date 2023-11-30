a = input().split()
b = input().split()
for i in b:
    if int(i) < int(a[1]):
        print(i,end=" ")