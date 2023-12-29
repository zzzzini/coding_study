n, q = map(int,input().split())
note = []
for i in range(n):
    for k in range(int(input())):
        note.append(i+1)
for i in range(q):
    print(note[int(input())])