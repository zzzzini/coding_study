def solution(s):
    n = len(s)
    answer = n

    for i in range(1, n//2 + 1):
        cnt = 1
        head = s[:i]
        temp = ''

        for j in range(i, n+i, i):
            if s[j:j+i] == head:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt) + head
                else:
                    temp += head

                head = s[j:j+i]
                cnt = 1

        if answer > len(temp):
            answer = len(temp)

    return answer