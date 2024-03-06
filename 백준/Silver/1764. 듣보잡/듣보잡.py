import sys
n, m = map(int, input().split())
dbj = {}
for i in range(n):
    listened = sys.stdin.readline().strip()
    if listened in dbj.keys():
        dbj[listened] += 1
    else:
        dbj[listened] = 1
for i in range(m):
    seen = sys.stdin.readline().strip()
    if seen in dbj.keys():
        dbj[seen] += 1
    else:
        dbj[seen] = 1
dbj = [k for k,v in dbj.items() if v == 2]
dbj.sort()
print(len(dbj))
for item in dbj:
    print(item)