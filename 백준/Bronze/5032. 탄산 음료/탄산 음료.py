a, b, c = map(int,input().split())
cnt = 0
sum = a+b
while True:
    cnt += sum // c
    if sum % c != 0:
        left = sum % c
    else:
        left = 0
    sum = sum // c + left
    if sum < c:
        break
print(cnt)