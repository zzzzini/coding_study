num = int(input())
for i in range(0,num,1):
    H, W, N = input().split()
    h, w, n = int(H), int(W), int(N)
    floor = n % h
    room = n // h + 1
    if n % h == 0:
        room = n // h
        floor = h
    print(floor*100 + room)