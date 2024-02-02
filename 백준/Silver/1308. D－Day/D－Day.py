import datetime
t_y, t_m, t_d = map(int, input().split())
d_y, d_m, d_d = map(int, input().split())

today = datetime.date(t_y, t_m, t_d)
dday = datetime.date(d_y, d_m, d_d)

timediff = int((dday-today).days)

for i in range(t_y, d_y+1, 1):
    if i % 4 == 0 and i % 100 != 0 and i % 400 == 0:
        if i == t_y:
            if t_m <= 2 and d_m > 2:
                timediff -= 1
        elif i == d_y:
            if d_m > 2:
                timediff -= 1
        else:
            timediff -= 1

flag = 1

if d_y - t_y > 1000:
    flag = 0
elif d_y - t_y == 1000:
    if d_m == t_m:
        if d_d >= t_d:
            flag = 0
    elif d_m > t_m:
        flag = 0


if flag:
    print(f"D-{timediff}")
else:
    print("gg")
