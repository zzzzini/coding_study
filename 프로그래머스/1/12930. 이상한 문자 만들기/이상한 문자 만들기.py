def solution(s):
    answer = ''
    cnt = 0
    for item in s:
        if item == ' ':
            cnt = 0
            answer += item
        else:
            if cnt % 2 == 0:
                answer += item.upper()
            else:
                answer += item.lower()
            cnt += 1
    return answer