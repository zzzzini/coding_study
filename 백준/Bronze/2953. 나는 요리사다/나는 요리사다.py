max = 0
index = 1
for i in range(0,5,1):
    score = list(map(int,input().split()))
    if sum(score) > max:
        max = sum(score)
        index = i + 1
print(index, max)