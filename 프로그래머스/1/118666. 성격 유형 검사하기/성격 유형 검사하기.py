def solution(survey, choices):
    mbti = { 'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0 }
    answer = ''
    for i in range(len(survey)):
        item = survey[i]
        item2 = choices[i]

        mbti[item[1]] += (item2 - (7//2 + 1))

    temp = list(mbti.keys())
    temp2 = list(mbti.values())
    key = [[]]
    score = [[]]
    for i in range(0, len(temp), 2):
        key.append([temp[i], temp[(i+1)]])
        score.append([temp2[i], temp2[(i+1)]])
    key.pop(0)
    score.pop(0)

    for i in range(len(key)):
        if score[i][0] > score[i][1]:
            answer += key[i][0]
        elif score[i][1] > score[i][0]:
            answer += key[i][1]
        elif score[i][0] == score[i][1]:
            key[i].sort()
            answer += key[i][0]

    return answer