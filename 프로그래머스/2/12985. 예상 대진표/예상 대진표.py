def solution(n, a, b):
    answer = 1
    if a > b:
        a, b = b, a

    while True:
        if b-a == 1 and a % 2 == 1:
            break

        if a % 2 == 1:
            a += 1
            a = a // 2
        else:
            a = a // 2

        if b % 2 == 1:
            b += 1
            b = b // 2
        else:
            b = b // 2

        answer += 1

    return answer