while True:
    a, b, c = map(int, input().split())
    if a==b==c==0:
        break
    else:
        if b-a == c-b:
            print("AP", c + b-a)
        elif b / a == c / b:
            print("GP", c * (b // a))