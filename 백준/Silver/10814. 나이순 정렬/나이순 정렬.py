import sys
input = sys.stdin.readline

answer = []
n = int(input())

for i in range(n):
    a,b = input().split()
    answer.append([int(a),i,b])
answer.sort()

for items in answer:
    print(items[0], items[2])