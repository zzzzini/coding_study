while True:
    num = input()
    cnt = 0
    if num == "0":
        break
    for i in range(0,len(num)//2,1):
        if num[i] != num[len(num)-(i+1)]:
            cnt += 1
    if cnt == 0:
        print("yes")
    else:
        print("no")