n = int(input())
num = list(map(int, input().split()))

answer = -1

for i in range(n+1):
    if i == num.count(i):
        answer = max(answer, i)

print(answer)