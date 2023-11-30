n = int(input())
left = 0
for i in range(0,n,1):
    a, b = map(int, input().split())
    left += b % a
print(left)