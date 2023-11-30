num = int(input())
cnt = 0
score = []
for i in range(0, num, 1):
    score.append(int(input()))
if score[0] >= max(score[1:]):
    print("S")
else:
    print("N")