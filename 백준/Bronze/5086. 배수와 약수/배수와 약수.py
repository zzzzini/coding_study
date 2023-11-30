while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if a % b == a and b % a == 0:
        print("factor")
    elif a % b == 0 and b % a == b:
        print("multiple")
    else:
        print("neither")