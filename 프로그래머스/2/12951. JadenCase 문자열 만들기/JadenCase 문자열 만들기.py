def solution(s):
    answer = ''
    counter = 1
    for item in s:
        if item == " ":
            answer += " "
            counter = 1
        else:
            if counter == 1:
                answer += item.upper()
                counter = 0
            else:
                answer += item.lower()
    return answer