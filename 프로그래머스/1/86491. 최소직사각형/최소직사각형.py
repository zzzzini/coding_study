def solution(sizes):
    answer = 0
    width = []
    height = []
    for item in sizes:
        item.sort()
        width.append(item[0])
        height.append(item[1])
    answer = max(width) * max(height)
    return answer