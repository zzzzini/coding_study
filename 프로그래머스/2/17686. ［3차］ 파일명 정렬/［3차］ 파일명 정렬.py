import re

def solution(files):
    answer = []
    key = []
    s = re.compile('[^0-9]*')
    n = re.compile('[0-9]*')
    for item in files:
        head = s.findall(item)[0].lower()
        new_item = item[len(head)::]

        number = int(n.findall(new_item)[0])
        key.append([item, head, number])

    key.sort(key=lambda x: (x[1], x[2]))

    for item in key:
        answer.append(item[0])
    return answer