n = int(input())
nums = list(map(int, input().split()))

nums = sorted(nums)
print(*nums)
nums = sorted(nums, reverse = True)
print(*nums)