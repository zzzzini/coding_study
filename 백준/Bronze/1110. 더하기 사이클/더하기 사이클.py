num = int(input())
nom = num
cnt = 0
while True:
    num = int((num%10)*10 + (num/10 + num%10)%10)
    cnt += 1
    if nom == num:
        break
print(cnt)