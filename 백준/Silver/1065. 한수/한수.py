n = int(input())
numbers = []
for i in range(100,n+1,1):
    if i == 1000:
        continue
    a = i // 100
    b = (i % 100) // 10
    c = (i % 100) % 10
    if a + c == 2 * b:
        numbers.append(i)
if n < 100:
    print(n)
else:
    print(len(numbers) + 99)