num = int(input())
std = []
for i in range(0,num,1):
    sum = 0
    cnt = 0
    score = list(input().split())
    for j in range(1,len(score),1):
        sum += int(score[j])
    avg = sum/int(score[0])
    for k in range(1,len(score),1):
        if float(score[k]) > avg:
            cnt += 1
    std.append(cnt/int(score[0])*100)
for i in std:
    print(f'{i:.3f}%')