def solution(answers):
    answer = []
    sol = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    for items in sol:
        idx = 0
        cnt = 0
        for item in answers:
            if item == items[idx]:
                cnt += 1
            if idx == len(items)-1:
                idx = 0
            else:
                idx += 1
        answer.append(cnt)
    answer = [k+1 for k, v in enumerate(answer) if v == max(answer)]
    return answer