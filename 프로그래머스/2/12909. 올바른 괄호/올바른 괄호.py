def solution(s):
    answer = True
    counter = 0
    for item in s:
        if counter < 0:
            answer = False
            break

        if item == "(":
            counter += 1
        else:
            counter -= 1

    if counter != 0:
        answer = False
    return answer