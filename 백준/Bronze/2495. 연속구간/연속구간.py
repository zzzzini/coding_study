for i in range(0,3,1):
    n = input()
    counter = 1
    max = 1
    for j in range(1,len(n),1):
        if n[j] == n[j-1]:
            counter += 1
            if counter > max:
                max = counter
        else:
            counter = 1
    print(max)