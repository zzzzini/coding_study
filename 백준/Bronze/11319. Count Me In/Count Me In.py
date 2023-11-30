n = int(input())
for i in range(0, n, 1):
    a = input()
    vow = 0
    blk = 0
    for j in range(0, len(a), 1):
        if a[j].lower() == "a" or a[j].lower() == "i" or a[j].lower() == a[j].lower() == "e" or a[j].lower() == "o" or a[j].lower() == "u":
            vow += 1
        elif a[j] == " ":
            blk += 1
    con = len(a) - (vow + blk)
    print(con, vow)