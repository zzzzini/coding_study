board = input()
answer = ''
count = 0
check = True
for i in range(len(board)):
    if board[i] == 'X':
        count += 1

    elif board[i] == '.':
        if count % 2 == 1:
            check = False
            break
        else:
            answer += ('AAAA' * (count // 4))
            answer += ('BB' * ((count % 4) // 2))
            answer += '.'
            count = 0

if count % 2 == 1:
    check = False

answer += ('AAAA' * (count // 4))
answer += ('BB' * ((count % 4) // 2))

if check:
    print(answer)
else:
    print(-1)