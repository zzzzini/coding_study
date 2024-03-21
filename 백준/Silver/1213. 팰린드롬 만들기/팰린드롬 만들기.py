t = input()
s = list(t)
s.sort()
dict = {}
for item in s:
    if item not in dict.keys():
        dict[item] = 1
    else:
        dict[item] += 1

answer = ''
for k, v in dict.items():
    for i in range(v//2):
        answer += k
    dict[k] -= (v//2 * 2)

temp = answer[-1::-1]

li = [k for k,v in dict.items() if v == 1]

if answer == temp[-1::-1] and (len(li) == 0 or len(li)) == 1:
    for item in li:
        answer += item
    print(answer + temp)
else:
    print("I'm Sorry Hansoo")