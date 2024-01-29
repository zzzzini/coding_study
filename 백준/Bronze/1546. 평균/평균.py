cnt = int(input())
score = list(map(int,input().split()))
max = 0
sum = 0.0
for i in range(0,cnt,1):
    if score[i] > max:
        max = score[i]
for i in range(0,cnt,1):
    score[i] = score[i]/max*100
    sum += score[i]
avg = sum/cnt
print(f'{avg:.2f}')