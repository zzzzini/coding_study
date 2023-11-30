n = list(map(int,input().split()))
n.sort()
s = input()
key = []
line = ['A','B','C']
for i in range(0,3,1):
    for j in range(0,3,1):
        if s[i] == line[j]:
            key.append(j)
for i in range(0,3,1):
    print(n[key[i]], end=' ')