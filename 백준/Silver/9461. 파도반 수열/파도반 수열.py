for i in range(int(input())):
    tri = [1,1,1]
    n = int(input())
    for j in range(3,n):
        tri.append(tri[j-3]+tri[j-2])
    print(tri[n-1])