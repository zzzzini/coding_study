n = int(input())
files = list(map(int, input().split()))
size = int(input())
counter = 0

for item in files:
    if item % size == 0:
        counter += (item//size)
    else:
        counter += ((item//size)+1)

print(size * counter)