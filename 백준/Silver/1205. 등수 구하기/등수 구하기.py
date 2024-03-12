n, t, p = map(int, input().split())
if n == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    score.append(t)
    score.sort(reverse=True)

    if score.index(t)+1 > p:
        print(-1)
    elif len([k for k in score if k>t]) + score.count(t) > p:
        print(-1)
    else:
        print(score.index(t)+1)