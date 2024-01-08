n = int(input())
numbers = list(map(int,input().split()))
s_numbers = set(numbers)
print(len(numbers) - len(s_numbers))