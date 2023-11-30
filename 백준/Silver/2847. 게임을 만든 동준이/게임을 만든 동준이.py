n = int(input())
score = []
for i in range(0,n,1):
    score.append(int(input()))
count = 0
for i in range(n-1,0,-1):
    if score[i-1] >= score[i]:
        counter = (score[i-1] - score[i]) + 1
        score[i-1] -= counter
        count += counter
print(count)