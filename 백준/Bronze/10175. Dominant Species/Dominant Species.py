n = int(input())
animal = ["Coyote","Bobcat","Wolf","Mountain Lion"]
for i in range(0,n,1):
    cnt = [0, 0, 0, 0]
    nd = 0
    dominant = "Coyote"
    land,dom = input().split()
    for j in range(0,len(dom),1):
        if dom[j] == "B":
            cnt[1] += 2
        elif dom[j] == "C":
            cnt[0] += 1
        elif dom[j] == "M":
            cnt[3] += 4
        elif dom[j] == "W":
            cnt[2] += 3
        else:
            exit()
    dominant = max(cnt)
    for j in range(0,len(cnt),1):
        if cnt[j] == dominant:
            nd += 1
    if nd == 1:
        print(land+": The "+animal[cnt.index(dominant)]+" is the dominant species")
    else:
        print(land+": There is no dominant species")