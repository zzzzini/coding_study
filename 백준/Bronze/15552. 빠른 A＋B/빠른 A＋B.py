import sys

T = int(sys.stdin.readline())
for i in range(0,T,1):
    a,b = sys.stdin.readline().split()
    A,B = int(a),int(b)
    print(A+B)