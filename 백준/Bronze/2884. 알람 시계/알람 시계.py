hour, minute = input().split()
H = int(hour)
M = int(minute)
if M-45 >= 0:
    print(H, M-45)
else:
    if H-1 >= 0:
        print(H-1, M+15)
    else:
        print(H+23, M+15)
