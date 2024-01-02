n, m, l = map(int, input().split())
people = [0 for i in range(n)]

people[0] += 1
no = 1
count = 0

while True:
    if people[no-1] == m:
        break

    count += 1
    if people[no-1] % 2 == 1:
        no += l
        if no > n:
            no -= n
        people[no-1] += 1

    else:
        no -= l
        if no < 1:
            no += n
        people[no-1] += 1

print(count)