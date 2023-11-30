card = list(map(int, input().split()))
if card[0] == card[1]:
    print(card[0])
else:
    if card[0] > card[1]:
        print(card[0])
    elif card[1] > card[0]:
        print(card[1])