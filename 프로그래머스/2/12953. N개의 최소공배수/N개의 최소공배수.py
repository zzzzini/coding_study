import math

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def solution(arr):
    answer = 1
    dict = {}
    for item in arr:
        temp = {}
        i = 2
        cnt = 0
        while True:
            if item == 1:
                temp[i] = cnt
                break
            if prime(i):
                if item % i == 0:
                    cnt += 1
                    item = item // i

                else:
                    temp[i] = cnt
                    cnt = 0
                    i += 1
            else:
                i += 1

        for k, v in temp.items():
            if k in dict.keys():
                dict[k] = max(dict[k],v)
            else:
                dict[k] = v

    for k, v in dict.items():
        answer *= (k ** v)

    return answer