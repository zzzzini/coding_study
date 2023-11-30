str = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    s = input()
    cnt = 0
    if s == "*":
        break
    for i in range(0,26,1):
        if str[i] not in s:
            cnt += 1
    if cnt >= 1:
        print("N")
    else:
        print("Y")