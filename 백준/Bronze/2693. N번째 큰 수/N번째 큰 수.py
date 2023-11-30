n = int(input())
for i in range(0,n,1):
    numbers = list(map(int,input().split()))
    numbers.sort(reverse=True)
    print(numbers[2])