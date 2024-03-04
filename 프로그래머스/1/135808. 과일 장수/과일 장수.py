def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    temp = score[m-1::m]
    for item in temp:
        answer += (m * item)
    return answer