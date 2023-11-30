A,B,C = input().split()
a,b,c = int(A),int(B),int(C)
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)