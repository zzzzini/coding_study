import math

TC = int(input())
answer = []

for i in range(TC):
    N = int(input())
    a = 0
    b = 0
    for j in range(1, round(math.sqrt(N))+1, 1):
        if N%j == 0:
            a = j
            b = N / a

    answer.append(int((a-1) + (b-1)))

for i in range(TC):
    print("#%d" %(i+1), end=' ')
    print(answer[i])