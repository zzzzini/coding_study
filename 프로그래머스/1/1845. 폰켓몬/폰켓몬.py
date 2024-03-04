def solution(nums):
    cnt = len(nums) // 2
    temp = set(nums)
    answer = len(temp) if cnt > len(temp) else cnt
    return answer