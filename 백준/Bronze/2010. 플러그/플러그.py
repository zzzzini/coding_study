import sys
input = sys.stdin.readline
n = int(input())
array = []
for i in range(0,n,1):
    array.append(int(input()))
print(sum(array) - (n-1))