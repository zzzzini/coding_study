T = int(input())
for i in range(1,T+1,1):
    a,b = input().split()
    A,B = int(a), int(b)
    print("Case #",i,": ",A+B,sep="")