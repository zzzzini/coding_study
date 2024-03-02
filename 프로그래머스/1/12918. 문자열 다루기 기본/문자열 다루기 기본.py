def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        answer = True
        for item in s:
            if ord(item) < 48 or ord(item) > 57:
                answer = False
    else:
        answer = False
    return answer