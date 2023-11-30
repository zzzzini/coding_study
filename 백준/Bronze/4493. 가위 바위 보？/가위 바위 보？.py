n = int(input())
for i in range(0,n,1):
    k = int(input())
    cnt = [0,0,0]
    for j in range(0,k,1):
        a, b = input().split()
        if a == b:
            cnt[0] += 1
        elif a == "R":
            if b == "P":
                cnt[2] += 1
            else:
                cnt[1] += 1
        elif a == "P":
            if b == "R":
                cnt[1] += 1
            else:
                cnt[2] += 1
        else:
            if b == "R":
                cnt[2] += 1
            else:
                cnt[1] += 1
    if cnt[1] == cnt[2]:
        print("TIE")
    elif cnt[1] > cnt[2]:
        print("Player 1")
    elif cnt[2] > cnt[1]:
        print("Player 2")