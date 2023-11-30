A,B,C = input().split()
a,b,c = int(A),int(B),int(C)
if a > b:
    big = a
else:
    big = b
if c > big:
    big = c
if a==b==c:
    print(10000+a*1000)
elif a==b or b==c:
    print(1000+b*100)
elif a==c:
    print(1000+a*100)
else:
    print(big*100)