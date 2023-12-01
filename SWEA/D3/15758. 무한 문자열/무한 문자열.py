n = int(input())
answer = []

for i in range(n):
    S, T = input().split()
    num = 0
    k = max(len(S), len(T))
    for j in range(k,(len(S)*len(T))+1, 1):
        if j%len(S) == 0 and j%len(T) == 0:
            num = j
            break

    t1 = ''
    t2 = ''
    for j in range(int(num/len(S))):
        t1 += S
    for j in range(int(num/len(T))):
        t2 += T
    if t1 == t2:
        answer.append('yes')
    else:
        answer.append('no')

for i in range(n):
    print('#%d' %(i+1), end=' ')
    print(answer[i])