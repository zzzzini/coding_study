def solution(data, ext, val_ext, sort_by):
    find = ['code', 'date', 'maximum', 'remain']
    answer = [[]]
    for item in data:
        if val_ext > item[find.index(ext)]:
            answer.append(item)
    answer.pop(0)
    answer.sort(key=lambda x:x[find.index(sort_by)])
    return answer