p, k = map(int, input().split())
answer = []
for i in range(2, k, 1):
    if p % i == 0:
        answer.append(i)

if len(answer) == 0:
    print("GOOD")
else:
    print("BAD", min(answer))