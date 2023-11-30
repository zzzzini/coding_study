import sys
input = sys.stdin.readline
n = int(input())
sum = 0
for i in range(0,n,1):
    a = int(input())
    sum += a-1
print(sum+1)