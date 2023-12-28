n, l, d = map(int, input().split())

music = 0
time = 0

for i in range(n):
    music += l

    if i != n-1:
        for j in range(music, music+5, 1):
            if j % d == 0:
                time = j
                break
    else:
        if music % d == 0:
            time = music
    if time != 0:
        break
    music += 5

if time == 0:
    time = (((n*l) + (5*(n-1)))//d)*d + d
print(time)