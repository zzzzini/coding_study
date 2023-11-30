n = int(input())
for i in range(0, n, 1):
    Y, K = 0, 0
    for j in range(0, 9, 1):
        y, k = map(int, input().split())
        Y += y
        K += k
    if Y > K:
        print("Yonsei")
    elif Y == K:
        print("Draw")
    else:
        print("Korea")