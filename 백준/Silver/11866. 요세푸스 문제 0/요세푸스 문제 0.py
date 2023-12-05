n, k = map(int, input().split())

count = 0
list = [i for i in range(1, n+1)]
answer = []
while list:
    count += k - 1
    if count >= len(list):
        count %= len(list)
    answer.append(str(list.pop(count)))

print("<", ", ".join(answer), ">", sep="")