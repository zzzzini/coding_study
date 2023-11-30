num = int(input())
for i in range(0,num,1):
    k = int(input())
    n = int(input())
    people = [x for x in range(1, n+1, 1)]
    for j in range(0,k,1):
        for t in range(1,n,1):
            people[t] += people[t-1]
    print(people[-1])