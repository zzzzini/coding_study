t = int(input())
one = 0
two = 0
for i in range(0,t,1):
    a, b = map(int,input().split())
    one = (b * 2) - a
    two = b - one
    print(one, two)