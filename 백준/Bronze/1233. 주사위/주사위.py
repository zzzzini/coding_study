a,b,c = map(int,input().split())

dict = {}
for i in range(a):
    for j in range(b):
        for k in range(c):
            key = (i+1)+(j+1)+(k+1)
            if dict.get(key):
                dict[key] += 1
            else:
                dict[key] = 1

answer = []
[answer.append(k) for k, v in dict.items() if v == max(dict.values())]
print(min(answer))