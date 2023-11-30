hour, minute = input().split()
time = int(input())
H = int(hour)
M = int(minute)
T = M+time
while T >= 60:
    if H < 23:
        T = T - 60
        H = H + 1
    else:
        T = T - 60
        H = H - 23
print(H, T)