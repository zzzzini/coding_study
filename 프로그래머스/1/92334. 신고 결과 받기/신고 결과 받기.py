def solution(id_list, report, k):
    answer = []
    dict = {key:[] for key in id_list}
    banned = {key:0 for key in id_list}
    report = set(report)
    for item in report:
        people, target = item.split()
        dict[people].append(target)
        banned[target] += 1

    bannedpeople = [key for key, v in banned.items() if v >= k]

    for i in range(len(id_list)):
        temp = dict[id_list[i]]
        cnt = 0
        for item in temp:
            if item in bannedpeople:
                cnt += 1
        answer.append(cnt)

    return answer