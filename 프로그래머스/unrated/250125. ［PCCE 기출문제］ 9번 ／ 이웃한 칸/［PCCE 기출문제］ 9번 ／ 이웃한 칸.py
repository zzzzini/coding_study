def solution(board, h, w):
    answer = 0
    find = board[h][w]
    if h > 0 and find == board[h-1][w] :
        answer += 1
    if h < len(board)-1 and find == board[h+1][w]:
        answer += 1
    if w > 0 and find == board[h][w-1]:
        answer += 1
    if w < len(board[h])-1 and find == board[h][w+1]:
        answer += 1
    return answer