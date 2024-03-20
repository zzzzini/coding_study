def solution(brown, yellow):
    answer = []
    target = (brown+4)//2
    list = []
    for i in range(target, target//2 - 1, -1):
        list.append([i, target - i])

    for item in list:
        if (item[0]-2) * (item[1]-2) == yellow:
            answer = [item[0], item[1]]
            break

    return answer