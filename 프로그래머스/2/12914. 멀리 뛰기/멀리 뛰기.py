def solution(n):
    li = []
    for i in range(n+1):
        if i == 0 or i == 1:
            li.append(1)
        else:
            li.append(li[i-1] + li[i-2])
    answer = li[-1] % 1234567
    return answer