n, m = map(int, input().split())
print(1 if n==1 else min(4,(m-1)//2+1) if n==2 else min(4,m) if m<7 else m-2)