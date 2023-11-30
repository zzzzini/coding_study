cnt = 0
for i in range(0, 6, 1):
    n = input()
    if n == "W":
        cnt += 1
if cnt < 1:
    print(-1)
elif 1 <= cnt <= 2:
    print(3)
elif 3 <= cnt <= 4:
    print(2)
elif 5 <= cnt <= 6:
    print(1)