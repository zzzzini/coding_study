def solution(n):
    answer = 0
    cnt = bin(n)[2:].count("1")
    while True:
        n += 1
        if bin(n)[2:].count("1") == cnt:
            answer = n
            break
    return answer