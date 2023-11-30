n = int(input())
num = []
for i in range(0,n,1):
    num.append(int(input()))
num.sort()
for i in range(0,n,1):
    print(num[i])