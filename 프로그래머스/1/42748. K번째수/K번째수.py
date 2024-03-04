def solution(array, commands):
    answer = []
    for item in commands:
        temp = array[item[0]-1:item[1]]
        temp.sort()
        answer.append(temp[item[2]-1])
    return answer