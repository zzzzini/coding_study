def solution(s):
    answer = ''
    dict = {
        "zero":"0", "one":"1", "two":"2", "three":"3", "four":"4",
        "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"
    }
    temp = ''
    for item in s:
        if item in dict.values():
            answer += item
            continue
        temp += item
        if temp in dict.keys():
            answer += dict[temp]
            temp = ''
    return int(answer)