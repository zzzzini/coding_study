def solution(arr):
    answer = []
    for item in arr:
        if len(answer) == 0:
            answer.append(item)
        elif answer[len(answer)-1] != item:
            answer.append(item)
    return answer