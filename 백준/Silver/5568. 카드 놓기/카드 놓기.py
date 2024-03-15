from itertools import permutations

n = int(input())
k = int(input())
cards = []
for i in range(n):
    cards.append(input())

numbers = list(permutations(cards, k))
answer = []

for items in numbers:
    temp = ''
    for item in items:
        temp += item
    answer.append(temp)

print(len(set(answer)))