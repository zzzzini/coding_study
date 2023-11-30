t = int(input())
for i in range(0,t,1):
    school = []
    number = []
    max = 0
    index = 0
    n = int(input())
    for j in range(0,n,1):
        s, num = input().split()
        school.append(s)
        number.append(int(num))
        if number[j] > max:
            max = number[j]
            index = j
    print(school[index])