num = input()
cnt = 0
while True:
    if len(num) == 1:
        break
    sum = 0
    cnt += 1
    for i in range(0,len(num),1):
        sum += int(num[i])
    num = str(sum)
print(cnt)
if int(num) % 3 == 0:
    print("YES")
else:
    print("NO")