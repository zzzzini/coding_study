n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = sorted(a)
d = sorted(b, reverse=True)
sum = 0
for i in range(0,n,1):
    sum += c[i] * d[i]
print(sum)