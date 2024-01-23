name = input()
teamname = []
point = []
n = int(input())
for i in range(n):
    love = [name.count("L"), name.count("O"), name.count("V"), name.count("E")]
    team = input()
    teamname.append(team)
    love[0] += team.count("L")
    love[1] += team.count("O")
    love[2] += team.count("V")
    love[3] += team.count("E")
    temp = 1
    for i in range(0,3,1):
        for j in range(i+1,4,1):
            temp *= (love[i]+love[j])
    point.append(temp % 100)

answer = []
for i in range(0,len(point),1):
    if point[i] == max(point):
        answer.append(teamname[i])
answer.sort()

print(answer[0])