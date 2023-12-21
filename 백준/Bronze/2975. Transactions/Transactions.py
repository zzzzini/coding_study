while True:
    a, b, c = list(input().split())
    if a == "0" and c == "0":
        break
    else:
        if b == "W":
            money = int(a) - int(c)
            if money < -200:
                print("Not allowed")
            else:
                print(money)
        else:
            money = int(a) + int(c)
            print(money)