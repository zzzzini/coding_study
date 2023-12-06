n,m=map(int,input().split())
board=[]
result=[]

for i in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        x=0
        y=0

        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2 == 0:
                    if board[k][l]!='B':
                        x+=1
                    elif board[k][l]!='W':
                        y+=1
                else:
                    if board[k][l]!='W':
                        x+=1
                    elif board[k][l]!='B':
                        y+=1

        result.append(x)
        result.append(y)

print(min(result))