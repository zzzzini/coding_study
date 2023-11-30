while True:
    A, B = input().split()
    a, b = int(A), int(B)
    if a > b:
        print("Yes")
    elif a == b == 0:
        break
    else:
        print("No")