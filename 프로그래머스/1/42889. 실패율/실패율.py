def solution(N, stages):
    answer = []
    record = [[i+1,0] for i in range(N)]
    temp = []
    count = 0
    stages.sort()
    for item in stages:
        if item not in temp:
            if item == N+1:
                count += 1
            else:
                record[item-1] = [item, stages.count(item)/(len(stages)-count)]
                count += stages.count(item)
                temp.append(item)
        else:
            continue
    record.sort(reverse = True, key = lambda x: x[1])
    for item in record:
        answer.append(item[0])
    return answer