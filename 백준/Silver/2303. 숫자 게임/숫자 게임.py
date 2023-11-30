n = int(input())
numbers = []
for i in range(0,n,1):
    m = 0
    nums = list(map(int, input().split()))
    for j in range(0,len(nums)-2,1):
        for k in range(j+1,len(nums)-1,1):
            for l in range(k+1,len(nums),1):
                if m < (nums[j] + nums[k] + nums[l]) % 10:
                    m = (nums[j] + nums[k] + nums[l]) % 10
    numbers.append(m)
counter = []
for i in range(0,len(numbers),1):
    if max(numbers) == numbers[i]:
        counter.append(i+1)
print(max(counter))