score = list(map(int, input().split()))
min = score[0]
index = 0
sum = score[0]
for i in range(1, 3, 1):
    if min > score[i]:
        min = score[i]
        index = i
    sum += score[i]
if sum < 100:
    if index == 0:
        print("Soongsil")
    elif index == 1:
        print("Korea")
    elif index == 2:
        print("Hanyang")
else:
    print("OK")