def solution(s):
    count = 0
    zeros = 0
    while True:
        if s == "1":
            break

        count += 1
        zeros += len(s)
        s = [k for k in s if k != "0"]
        zeros -= len(s)

        c = len(s)
        s = str(bin(c)[2:])

    answer = [count, zeros]
    return answer