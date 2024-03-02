import math
def solution(n, m):
    answer = []
    ns = []
    ms = []

    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0 and i not in ns:
            ns.append(i)
            ns.append(n//i)

    for i in range(1, int(math.sqrt(m))+1):
        if m % i == 0 and i not in ms:
            ms.append(i)
            ms.append(m//i)

    li = [k for k in ns if k in ms]
    answer.append(max(li))
    answer.append(n*m//answer[0])

    return answer