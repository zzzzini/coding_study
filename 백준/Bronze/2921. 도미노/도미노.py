n = int(input())
sum = 0
for i in range(1,n+1,1):
    sum += i * (i+1)
    sum += i * (n-i+1)
print(sum)