TC = int(input())
answer = []

for i in range(TC):
    N = int(input())
    if N%2 == 0:
        answer.append('Alice')
    else:
        answer.append('Bob')

for i in range(TC):
    print('#%d' %(i+1), end=' ')
    print(answer[i])