from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    originalone = deque()

    onehap = sum(queue1)
    twohap = sum(queue2)
    hap = onehap + twohap

    if hap % 2 == 1:
        answer = -1

    else:
        while queue1 and queue2:
            
            if hap // 2 == onehap:
                return answer

            elif onehap > hap // 2:
                target = queue1.popleft()
                onehap -= target
                answer += 1
            else:
                target = queue2.popleft()
                queue1.append(target)
                onehap += target
                answer += 1

    return -1