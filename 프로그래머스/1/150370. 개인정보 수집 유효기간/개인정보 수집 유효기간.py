def solution(today, terms, privacies):
    year = int(today[0:4])
    month = int(today[5:7])
    day = int(today[8:10])
    answer = []
    n_t = {}
    for item in terms:
        key = item[0]
        value = item[2::]
        n_t[key] = int(value)
    no = 0
    for item in privacies:
        p_y = int(item[0:4])
        p_m = int(item[5:7])
        p_d = int(item[8:10])
        p_p = item[-1]

        p_m += n_t[p_p]
        p_d -= 1

        if p_d == 0:
            p_m -= 1
            p_d = 28

        if p_m > 12:
            advantage = p_m//12
            p_y += advantage
            p_m -= 12*advantage

        if p_m == 0:
            p_y -= 1
            p_m += 12

        idx = no + 1

        if year > p_y or (year == p_y and (month > p_m or (month == p_m and day > p_d))):
            answer.append(idx)

        no += 1

    return answer