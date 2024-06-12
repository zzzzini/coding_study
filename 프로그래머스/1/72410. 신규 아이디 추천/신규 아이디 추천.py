def solution(new_id):
    answer = ''
    temp = ''
    characters = ['-','_','.']
    # 규칙 1
    new_id = new_id.lower()
    # 규칙 2
    for item in new_id:
        if 48 <= ord(item) <= 57 or 97 <= ord(item) <= 122 or item in characters:
            temp += item
    # 규칙 3
    for item in temp:
        if len(answer) > 0:
            if answer[-1] == '.' and item == '.':
                pass
            else:
                answer += item
        else:
            answer += item
    # 규칙 4
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 규칙 5,6
    if len(answer) == 0:
        answer = 'a'
    elif len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    # 규칙 7
    if len(answer) <= 2:
        while True:
            answer += answer[-1]
            if len(answer) == 3:
                break
    return answer