TC = int(input())
answer = []

for i in range(TC):
    S = input()
    count = 0
    for j in range(0, len(S), 1):
        if S[j] == ')':
            count += 1
        elif S[j] == '(':
            if S[j+1] != ')':
                count += 1

    answer.append(count)

for i in range(TC):
    print('#%d' %(i+1), end=' ')
    print(answer[i])