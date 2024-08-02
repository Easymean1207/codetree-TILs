def recursiveMax(nums):
    if len(nums) == 1:
        return nums[0]
    
    max_of_rest = recursiveMax(nums[:-1])
    return max(nums[-1], max_of_rest)

n = int(input())

nums = list(map(int, input().split()))

print(recursiveMax(nums))