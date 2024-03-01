def solution(d, budget):
    answer = 0
    d.sort()
    for item in d:
        if item > budget:
            break
        else:
            budget -= item
            answer += 1
    return answer