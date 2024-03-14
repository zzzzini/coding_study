def solution(n):
    answer = 0
    numbers = [k for k in range(1, n+1)]
    for i in range(1, n+1):
        if sum(numbers[:i]) > n:
            break

        if i % 2 == 1:
            if sum(numbers[(n//i)-(i//2)-1:(n//i)+(i//2)]) == n:
                answer += 1

        else:
            if sum(numbers[(n//i)-(i//2):(n//i)+(i//2)]) == n:
                answer += 1
    return answer