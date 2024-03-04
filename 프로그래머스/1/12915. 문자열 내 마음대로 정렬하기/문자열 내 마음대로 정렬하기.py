def solution(strings, n):
    answer = []
    dict = {}
    for item in strings:
        temp = item[n]
        if temp not in dict.keys():
            dict[temp] = [item]
        else:
            dict[temp].append(item)
    for item in dict.values():
        item.sort()

    key = sorted(dict.keys())
    for items in key:
        for item in dict[items]:
            answer.append(item)
    return answer