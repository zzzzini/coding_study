def solution(s):
    answer = ''
    low = []
    up = []
    for item in s:
        if ord(item) >= 97:
            low.append(item)
        else:
            up.append(item)
    low.sort(reverse=True)
    up.sort(reverse=True)
    for item in low:
        answer += item
    for item in up:
        answer += item
    return answer