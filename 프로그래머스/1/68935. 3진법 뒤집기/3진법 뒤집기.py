def solution(n):
    answer = ''
    while True:
        if n < 3:
            answer += str(n)
            break
        a, b = divmod(n, 3)
        answer += str(b)
        n = a
    answer = int(answer, 3)
    return answer