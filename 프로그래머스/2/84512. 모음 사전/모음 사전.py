from itertools import product

def solution(word):
    temp = []
    li = ['A','E','I','O','U']
    for i in range(1,6):
        for item in product(li,repeat=i):
            temp.append(''.join(item))

    temp.sort()
    answer = temp.index(word) + 1
    return answer