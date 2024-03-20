def solution(n, words):
    answer = [0, 0]
    wordlist = []
    round = 1
    ind = 1
    for i in range(len(words)):
        if i == 0:
            wordlist.append(words[i])
        else:
            if len(words[i]) == 1 or words[i-1][-1] != words[i][0] or words[i] in wordlist:
                answer = [ind, round]
                break
            else:
                wordlist.append(words[i])
        ind += 1
        if ind > n:
            round += 1
            ind = 1
    return answer