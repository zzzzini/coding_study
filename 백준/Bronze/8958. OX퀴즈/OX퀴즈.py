num = int(input())
oxs = []
for i in range(0,num,1):
    sum = 0
    no = 0
    its = list(input())
    for i in range(0,len(its),1):
        if its[i] == "O":
            no += 1
            sum += no
        else:
            no = 0
    oxs.append(sum)
for i in range(0,num,1):
    print(oxs[i])