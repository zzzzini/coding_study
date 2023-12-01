TC = int(input())
answer = []

for i in range(TC):
    N = int(input())
    S = input()

    if S[:int(N/2)] == S[int(N/2):]:
        answer.append("Yes")
    else:
        answer.append("No")

for i in range(TC):
    print("#%d" %(i+1), end=' ')
    print(answer[i])