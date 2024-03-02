def solution(price, money, count):
    li = [k+1 for k in range(count)]
    cost = price * sum(li)
    if cost - money > 0:
        answer = cost - money
    else:
        answer = 0

    return answer