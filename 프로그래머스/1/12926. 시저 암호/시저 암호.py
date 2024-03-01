def solution(s, n):
    answer = ''
    for item in s:
        if item == ' ':
            answer += ' '
        else:
            if ord(item) >= 97 and ord(item) + n > 122:
                answer += chr(ord(item) + n - 26)
            elif ord(item) <= 90 and ord(item) + n > 90:
                answer += chr(ord(item) + n - 26)
            else:
                answer += chr(ord(item) + n)
    return answer