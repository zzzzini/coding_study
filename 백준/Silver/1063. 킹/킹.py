king, stone, n = input().split()
move_dict = {
    'R': [1,0],
    'L': [-1,0],
    'B': [0,-1],
    'T': [0,1],
    'RT': [1,1],
    'LT': [-1,1],
    'RB': [1,-1],
    'LB': [-1,-1]
}
for i in range(int(n)):
    move = move_dict[input()]
    if 65 <= ord(king[0]) + move[0] <= 72 and 1 <= int(king[1]) + move[1] <= 8:
        king = chr(ord(king[0])+move[0]) + str(int(king[1])+move[1])
        if king == stone:
            if 65 <= ord(stone[0]) + move[0] <= 72 and 1 <= int(stone[1]) + move[1] <= 8:
                stone = chr(ord(king[0])+move[0]) + str(int(king[1])+move[1])
            else:
                king = chr(ord(king[0])-move[0]) + str(int(king[1])-move[1])

print(king)
print(stone)