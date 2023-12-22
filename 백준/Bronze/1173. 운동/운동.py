N, m, M, T, R = map(int, input().split())
time = 0
work = 0
pulse = m
if m+T > M:
    print(-1)
else:
    while N > work:
        if M >= pulse+T:
            pulse += T
            work += 1
            time += 1
        else:
            pulse -= R
            if m > pulse:
                pulse = m
            time += 1
    print(time)