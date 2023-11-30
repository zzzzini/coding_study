i = 1
while True:
    if i != 1:
        print()
    a, b, c= map(int,input().split())
    if a == b == c == 0:
        break
    print("Triangle #", end='')
    print(i)
    if c != -1 and (c < a or c < b or a == c or b == c):
        print("Impossible.")
    elif a == -1:
        print("a = %.3f" %((c**2-b**2)**0.5))
    elif b == -1:
        print("b = %.3f" %((c**2-a**2)**0.5))
    elif c == -1:
        print("c = %.3f" %((a**2+b**2)**0.5))
    i += 1