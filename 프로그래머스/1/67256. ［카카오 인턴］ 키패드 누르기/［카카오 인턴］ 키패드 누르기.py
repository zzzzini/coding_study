def solution(numbers, hand):
    answer = ''
    array = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    num = 1
    l = [1, 4, 7]
    r = [3, 6, 9]

    lf = [3,0]
    rf = [3,2]
    point = [0,0]

    for items in numbers:
        if items in l:
            answer += 'L'
            lf = [l.index(items), 0]
        elif items in r:
            answer += 'R'
            rf = [r.index(items), 2]
        else:
            point = [[i, j] for i in range(4) for j in range(3) if array[i][j] == items][0]
            ld = abs(point[0]-lf[0]) + abs(point[1]-lf[1])
            rd = abs(point[0]-rf[0]) + abs(point[1]-rf[1])
            if ld > rd:
                answer += 'R'
                rf = point
            elif rd > ld:
                answer += 'L'
                lf = point
            else:
                if hand == 'right':
                    answer += 'R'
                    rf = point
                else:
                    answer += 'L'
                    lf = point
        print(lf, rf)

    return answer