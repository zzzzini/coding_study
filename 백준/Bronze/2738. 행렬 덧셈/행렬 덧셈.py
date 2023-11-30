import sys
n,m=map(int,sys.stdin.readline().strip().split())
arr1=[[0]*m for _ in range(n)]
arr2=[[0]*m for _ in range(n)]
for i in range(n):
    arr1[i]=list(map(int,sys.stdin.readline().strip().split()))
for i in range(n):
    arr2[i]=list(map(int,sys.stdin.readline().strip().split()))
    
print("\n".join(" ".join(str(e1+e2) for e1,e2 in zip(arr1[i],arr2[i])) for i in range(n)))