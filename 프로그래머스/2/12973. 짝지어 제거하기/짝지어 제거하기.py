def solution(s):
    li = []
    for item in s:
        if len(li) == 0:
            li.append(item)

        elif li[-1] == item:
                li.pop()
        else:
            li.append(item)

    if len(li) == 0:
        answer = 1
    else:
        answer = 0

    return answer