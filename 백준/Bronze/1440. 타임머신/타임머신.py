time = list(map(int, input().split(":")))

count = 0
no = True

for i in range(len(time)):
    if time[i] >= 0 and time[i] < 60:
        if time[i] >= 1 and time[i] <= 12:
            count += 2

    else:
        no = False

if no:
    print(count)
else:
    print(0)