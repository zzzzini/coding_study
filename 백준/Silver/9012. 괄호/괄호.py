n = int(input())
answer = []
for i in range(n):
    line = input()
    count = 0
    bool = True

    if len(line)%2 != 0:
        answer.append("NO")
        continue
    else:
        for item in line:
            if item == "(":
                count += 1
            elif item == ")":
                count -= 1
            if count < 0:
                answer.append("NO")
                bool = False
                break
        if count == 0:
            answer.append("YES")
        elif count > 0 and bool:
            answer.append("NO")

for item in answer:
    print(item)