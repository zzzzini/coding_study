s = input().lower()
distinct = []
for i in range(0,len(s),1):
    if s[i] not in distinct:
        distinct.append(s[i])
counter = [0] * len(distinct)
for i in range(0,len(distinct),1):
    for j in range(0,len(s),1):
        if distinct[i] == s[j]:
            counter[i] += 1
max = 0
index = 0
for i in range(0,len(counter),1):
    if counter[i] > max:
        max = counter[i]
        index = i
counter.remove(max)
if max in counter:
    print("?")
else:
    print(distinct[index].upper())