def solution(a, b, n):
    answer = 0
    while True:
        if n < a:
            break

        p, q = divmod(n, a)
        answer += p * b
        n = p * b + q
    return answer

print(solution(3, 1, 20))