TC = int(input())
answer = []

for i in range(TC):
    N = int(input())
    answer.append(N**2)

for i in range(TC):
    print("#%d" %(i+1), end=' ')
    print(answer[i])