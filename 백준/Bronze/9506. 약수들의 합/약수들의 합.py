while True:
    n = int(input())
    sum = 0
    first = []
    last = []
    if n == -1:
        break
    for i in range(1,n//2,1):
        if n % i == 0:
            first.append(i)
            if n//i != n:
                last.append(n//i)
    for i in range(0, len(last), 1):
        if last[len(last)-(i+1)] not in first:
            first.append(last[len(last)-(i+1)])
    for i in range(0, len(first), 1):
        sum += first[i]
    if n == sum:
        print(n, "= ", end='')
        for i in range(0, len(first)-1, 1):
            print(first[i], "+ ", end='')
        print(first[len(first)-1])
    else:
        print(n, "is NOT perfect.")