li = []
n = int(input())

for i in range(n):
    li.append(input())

for i in range(n-1):
    for j in range(i+1,n):
        if len(li[i]) > len(li[j]):
            li[i], li[j] = li[j], li[i]

        elif len(li[i]) == len(li[j]):
            leftsum = 0
            rightsum = 0
            for k in range(len(li[i])):
                if not 65<=ord(li[i][k])<=90:
                    leftsum += int(li[i][k])
                if not 65<=ord(li[j][k])<=90:
                    rightsum += int(li[j][k])

            if leftsum > rightsum:
                li[i], li[j] = li[j], li[i]
            elif leftsum == rightsum:
                li[i], li[j] = sorted([li[i], li[j]])[0], sorted([li[i], li[j]])[1]

for item in li:
    print(item)