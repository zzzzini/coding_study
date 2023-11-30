cnt = int(input())
core = list(map(int,input().split()))
max = 0
sum = 0.0
for i in range(0,cnt,1):
    if core[i] > max:
        max = core[i]
for i in range(0,cnt,1):
    core[i] = core[i]/max*100
    sum += core[i]
avg = sum/cnt
print(f'{avg:.2f}')