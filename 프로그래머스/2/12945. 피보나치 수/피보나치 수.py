def solution(n):
    li = [0,1]
    for i in range(2, n+1):
        li.append(li[-1] + li[-2])
    answer = li.pop() % 1234567
    return answer