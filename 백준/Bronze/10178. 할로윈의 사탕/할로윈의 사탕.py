n = int(input())
for i in range(0,n,1):
    num = list(map(int, input().split()))
    son = int(num[0]/num[1])
    dad = num[0] % num[1]
    print("You get", son, "piece(s) and your dad gets", dad, "piece(s).")