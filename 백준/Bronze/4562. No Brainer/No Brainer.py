n = int(input())
for i in range(0, n, 1):
    A, B = input().split()
    a, b = int(A), int(B)
    if a < b:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")