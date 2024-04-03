x = int(input())
li = [0,0]

for i in range(2,x+1):
    temp = li[i-1]
    if i % 2 == 0:
        temp = min(temp, li[i//2])
    if i % 3 == 0:
        temp = min(temp, li[i//3])
    li.append(temp+1)

print(li.pop())