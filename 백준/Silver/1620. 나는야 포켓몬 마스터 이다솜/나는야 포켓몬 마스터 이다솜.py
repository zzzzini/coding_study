import sys
n, m = map(int,input().split())
dict = {}
for i in range(n):
    dict[f'{i+1}'] = sys.stdin.readline().strip()
rev = {v:k for k, v in dict.items()}
for i in range(m):
    q = sys.stdin.readline().strip()
    if dict.get(q):
        print(dict.get(q))
    else:
        print(rev.get(q))