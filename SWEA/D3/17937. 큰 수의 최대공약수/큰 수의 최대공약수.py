T = int(input())
answer = []

for i in range(T):
    A, B = map(int, input().split())
    num = 0
    if A == B:
        num = A
    else:
        num = 1

    answer.append(num)

for i in range(T):
    print('#%d' %(i+1), end=' ')
    print(answer[i])