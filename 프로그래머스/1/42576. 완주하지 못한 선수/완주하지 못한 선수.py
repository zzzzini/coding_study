def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    flag = True
    while completion:
        if participant[-1] == completion[-1]:
            participant.pop()
            completion.pop()
        else:
            break
    answer = participant.pop()
    return answer