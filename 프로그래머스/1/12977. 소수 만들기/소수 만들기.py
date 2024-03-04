def solution(nums):
    answer = 0
    li = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                li.append(nums[i]+nums[j]+nums[k])

    print(li)
    for item in li:
        flag = True
        for i in range(2, item):
            if item % i == 0:
                flag = False
                break
        if flag:
            answer += 1
    return answer