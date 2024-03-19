n, m, k = map(int, input().split())
scoredict = {}
for i in range(m):
    ability = list(input().split())
    for j in range(0,len(ability),2):
        if ability[j] in scoredict.keys():
            scoredict[ability[j]] = max(scoredict[ability[j]], float(ability[j+1]))
        else:
            scoredict[ability[j]] = float(ability[j+1])

val = list(scoredict.values())
val.sort(reverse=True)
print(round(sum(val[:k]), 1))