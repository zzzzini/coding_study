A,B,C = input().split()
a,b,c = int(A),int(B),int(C)
move = c - a
if move % (a-b) == 0:
    day = int(move/(a-b))
else:
    day = int(move/(a-b) + 1)
print(day + 1)