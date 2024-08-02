def recursiveMax(nums):
    # 원소가 하나라면 그 값이 최대(종료 조건)
    if len(nums) == 1:
        return nums[0]
    
    # 마지막 원소 (첫번째 ~ 마지막 -1)원소들을 비교하여
    # 최대값을 찾는 과정을 반복
    max_of_rest = recursiveMax(nums[:-1])
    return max(nums[-1], max_of_rest)

n = int(input())

nums = list(map(int, input().split()))

print(recursiveMax(nums))