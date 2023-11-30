M = int(input())
N = int(input())
list = []
for i in range(M,N+1,1):
    for j in range(2,int(i**1/2)+1,1):
        if i % j == 0:
            break
    else:
        if i != 1:
            list.append(i)
if len(list) == 0:
    print(-1)
else:
    print(sum(list))
    print(list[0])