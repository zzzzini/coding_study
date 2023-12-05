a, b = map(int, input().split())
head = 1
bottom = 1
for i in range(a):
    head *= (i+1)
for i in range(b):
    bottom *= (i+1)
for i in range(a-b):
    bottom *= (i+1)
print(head // bottom)