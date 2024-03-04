import math
def solution(number, limit, power):
    answer = 0
    str = []
    for i in range(1, number+1):
        li = set()
        for j in range(1, int(math.sqrt(i))+1, 1):
            if i % j == 0:
                li.add(j)
                li.add(i//j)
        str.append(len(li))

    for item in str:
        if item > limit:
            answer += power
        else:
            answer += item
    return answer