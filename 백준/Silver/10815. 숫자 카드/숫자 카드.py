import sys
n = sys.stdin.readline()
cards = set(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline()
find = list(map(int, sys.stdin.readline().split()))

for items in find:
    if items in cards:
        print("1", end=' ')
    else:
        print("0", end=' ')