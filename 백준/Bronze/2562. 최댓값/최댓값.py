num = [0,0,0,0,0,0,0,0,0]
max = 0
for i in range(0,9,1):
    num[i] = int(input())
    if num[i] > max:
        max = num[i]
        index = i+1
print(max)
print(index)
