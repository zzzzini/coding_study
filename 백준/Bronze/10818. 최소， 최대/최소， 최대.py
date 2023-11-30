num = int(input())
team = input().split()
max = int(team[0])
min = int(team[0])
for i in range (1,num,1):
    if int(team[i]) > max:
        max = int(team[i])
    elif int(team[i]) < min:
        min = int(team[i])
print(min, max)
