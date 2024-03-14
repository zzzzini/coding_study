def solution(s):
    answer = ''
    temp = s.split()
    li = []
    for item in temp:
        li.append(int(item))
    li.sort()
    answer = str(li[0]) + " " + str(li[len(li)-1])
    return answer