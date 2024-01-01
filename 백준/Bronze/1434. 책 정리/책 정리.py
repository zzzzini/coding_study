n, m = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))

no = 0
for i in range(len(book)):
    if box[no] >= book[i]:
        box[no] -= book[i]
    else:
        while book[i] > box[no]:
            no += 1
        box[no] -= book[i]

print(sum(box))