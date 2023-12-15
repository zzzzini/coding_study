def solution(board, moves):
    answer = 0
    basket = []
    for item in moves:
        for i in range(len(board)):
            if board[i][item-1] == 0:
                continue
            else:
                basket.append(board[i][item-1])
                board[i][item-1] = 0
                break

        if len(basket) >= 2 and basket[len(basket)-1] == basket[len(basket)-2]:
            basket.pop()
            basket.pop()
            answer += 2
    return answer