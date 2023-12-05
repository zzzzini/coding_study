import sys
input = sys.stdin.readline

answer = []
n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    answer.append([a,b])
answer.sort()

for items in answer:
    print(items[0], items[1])