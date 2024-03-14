def solution(babbling):
    answer = 0
    two = ["ye", "ma"]
    three = ["aya", "woo"]
    for i in range(len(babbling)):
        key = ''
        while True:
            if len(babbling[i]) == 0:
                answer += 1
                break
            if babbling[i][:2] in two and key != babbling[i][:2]:
                key = babbling[i][:2]
                babbling[i] = babbling[i][2:]
            elif babbling[i][:3] in three and key != babbling[i][:3]:
                key = babbling[i][:3]
                babbling[i] = babbling[i][3:]
            else:
                break

    return answer