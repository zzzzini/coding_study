Adrian = 'ABCABC' * 20
Bruno = 'BABC' * 25
Goran = 'CCAABB' * 20

Sang, Chang, Hyeon = 0, 0, 0

N = int(input())
answer = input()

for i in range(N):
    if answer[i:i+1] == Adrian[i:i+1]:
        Sang += 1
    if answer[i:i+1] == Bruno[i:i+1]:
        Chang += 1
    if answer[i:i+1] == Goran[i:i+1]:
        Hyeon += 1

max_score = max(Sang, Chang, Hyeon)

print(max_score)
if Sang == max_score:
    print('Adrian')
if Chang == max_score:
    print('Bruno')
if Hyeon == max_score:
    print('Goran')