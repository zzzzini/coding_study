n = int(input())
li = []
score = []

for i in range(n):
    li.append(int(input()))

for i in range(1,n+1):
    if i == 1:
        score.append([li[i-1], li[i-1]])
    elif i == 2:
        score.append([li[i-2]+li[i-1], li[i-1]])
    else:
        score.append([score[i-2][1]+li[i-1], max(score[i-3][0], score[i-3][1])+li[i-1]])
print(max(score[n-1][0], score[n-1][1]))