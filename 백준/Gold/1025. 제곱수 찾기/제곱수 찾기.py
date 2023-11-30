n, m = map(int, input().split(' '))

matrix = []

for i in range(n):
    matrix.append(list(map(int, list(input()))))


def solution(n, m, matrix):
    max_square = -1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] ** 0.5 == int(matrix[i][j] ** 0.5):
                max_square = max(max_square, matrix[i][j])

    n_list = list(range(-n + 1, n))
    m_list = list(range(-m + 1, m))

    every_combinations = []
    for ele1 in n_list:
        for ele2 in m_list:
            every_combinations.append([ele1, ele2])
    every_combinations = reversed(every_combinations)

    res = []
    for combination in every_combinations:
        n_difference, m_difference = combination
        if n_difference == 0 and m_difference == 0:
            continue

        for i in range(n):
            for j in range(m):
                current_int = ""
                pick_up = [i, j]

                while 0 <= pick_up[0] < n and 0 <= pick_up[1] < m:
                    current_int += str(matrix[pick_up[0]][pick_up[1]])
                    res.append(int(current_int))
                    pick_up[0] += n_difference
                    pick_up[1] += m_difference

    for ele in res:
        if ele ** 0.5 == int(ele ** 0.5):
            max_square = max(max_square, ele)

    return max_square


print(solution(n, m, matrix))