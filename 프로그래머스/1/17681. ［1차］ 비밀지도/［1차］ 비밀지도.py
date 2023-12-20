def solution(n, arr1, arr2):
    answer = ["" for i in range(n)]
    map1 = []
    map2 = []
    for item in arr1:
        temp = []
        while item > 1:
            temp.append(item%2)
            item = item // 2
        temp.append(item)
        while n > len(temp):
            temp.append(0)
        temp.reverse()
        map1.append(temp)

    for item in arr2:
        temp = []
        while item > 1:
            temp.append(item%2)
            item = item // 2
        temp.append(item)
        while n > len(temp):
            temp.append(0)
        temp.reverse()
        map2.append(temp)

    for i in range(n):
        for j in range(n):
            if map1[i][j] == 1 or map2[i][j] == 1:
                answer[i] += "#"
            else:
                answer[i] += " "
    return answer