def numSort(input_nums):
    return input_nums.sort()


N, K = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
numSort(nums)

print(nums[K-1])