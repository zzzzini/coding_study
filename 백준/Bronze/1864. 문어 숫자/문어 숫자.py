s = ['-','\\','(','@','?','>','&','%','/']
num = [0,1,2,3,4,5,6,7,-1]
while True:
    str = input()
    sum = 0
    key = 0
    adv = 1
    if str == "#":
        break
    for i in range(0,len(str),1):
        for j in range(0,len(s),1):
            if str[i] == s[j]:
                key = j
                adv = num[key]
        for j in range(len(str)-i,1,-1):
            adv *= 8
        sum += adv
    print(sum)