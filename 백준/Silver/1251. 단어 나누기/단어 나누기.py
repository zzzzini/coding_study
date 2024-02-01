s = input()
answer = []

for i in range(1, len(s), 1):
    for j in range(i+1, len(s), 1):
        first = s[:i]
        second = s[i:j]
        third = s[j:]

        new = first[::-1] + second[::-1] + third[::-1]
        answer.append(new)

answer.sort()
print(answer[0])