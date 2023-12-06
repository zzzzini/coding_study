from collections import deque
n = int(input())
array = deque()
for i in range(n):
    array.append(i+1)
while len(array) > 1:
    array.popleft()
    array.append(array.popleft())
print(array[0])