n, m = map(int, input().split())
li = []
answer = ''
cnt = 0

for i in range(n):
    li.append(input())

for i in range(m):
    dict = {'A':0, 'C':0, 'G':0, 'T':0}
    for item in li:
        dict[item[i]] += 1
    s = [k for k, v in dict.items() if v == max(dict.values())]
    answer += s[0]
    cnt += (sum(dict.values()) - max(dict.values()))

print(answer)
print(cnt)