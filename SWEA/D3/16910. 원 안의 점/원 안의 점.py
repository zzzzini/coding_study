T = int(input())
answer = []

for i in range(T):
    N = int(input())

    counter = 0
    for j in range(-N, N+1, 1):
        for k in range(-N, N+1, 1):
            if N**2 >= j**2 + k**2:
                counter += 1

    answer.append(counter)

for i in range(T):
    print('#%d' %(i+1), end=' ')
    print(answer[i])