x = int(input())
i = 1

while True:
    if i >= 1000000:
        print(0)
        break
    else:
        if sorted(str(i)) == sorted(str(x)) and i > x:
            print(i)
            break
    i += 1