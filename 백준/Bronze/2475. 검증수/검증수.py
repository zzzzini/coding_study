a = list(map(int, input().split()))
sum = 0
for i in range(0,len(a),1):
    sum += a[i] ** 2
print(sum % 10)