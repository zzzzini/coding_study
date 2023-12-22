x = {}
n = int(input())
for i in range(n):
    val = input()
    temp = val[0]
    if x.get(temp):
        x[temp] = x[temp] + 1
    else:
        x[temp] = 1
temp = []
index = 0
for key, val in x.items():
    if int(val) >= 5:
        temp.append(key)
temp.sort()
answer = ""
for i in temp:
    answer += i
if answer == "":
    print("PREDAJA")
else:
    print(answer)