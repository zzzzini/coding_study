import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
dict = {}
for i in range(n):
    domain, pw = sys.stdin.readline().rstrip().split()
    dict[domain] = pw
for i in range(m):
    key = sys.stdin.readline().rstrip()
    print(dict[key])