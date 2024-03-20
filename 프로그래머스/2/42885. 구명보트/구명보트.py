def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    i = 0

    while True:
        if i >= len(people):
            break

        if limit >= people[i] + people[-1]:
            people.pop()

        answer += 1
        i += 1

    return answer