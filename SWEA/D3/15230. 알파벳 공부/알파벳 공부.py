n = int(input())
alpha = []
num = 97
answer = []

for i in range(26):
    alpha.append(chr(num))
    num += 1

for i in range(n):
    s = input()
    cnt = 0

    for j in range(len(s)):
        if (s[j] != alpha[j]):
            break
        else:
            cnt += 1

    answer.append(cnt)

for i in range(n):
    print('#%d' %(i+1), end=' ')
    print(answer[i])