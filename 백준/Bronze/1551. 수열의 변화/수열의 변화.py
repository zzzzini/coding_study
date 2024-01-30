n, k = map(int, input().split())
li = list(map(int, input().split(',')))

for i in range(k):
    temp = []
    for i in range(1, len(li), 1):
        temp.append(li[i]-li[i-1])
    li = temp

for i in range(len(li)):
    if i == len(li)-1:
        print(li[i])
    else:
        print(li[i],end=',')