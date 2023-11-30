n = int(input())
s = []
index = []
num = 4
for i in range(0,n,1):
    name, no = input().split()
    s.append(name)
    index.append(int(no))
for i in range(0,n,1):
    if index[i] <= num:
        num = index[i]
        min = s[i]
print(min)