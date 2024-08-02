def recursiveMultiply(n):
    if n <= 10:
        return n
    
    return recursiveMultiply(n//10) + n%10


nums = tuple(map(int, input().split()))
product = 1

for i in range(len(nums)):
    product *= nums[i]

print(recursiveMultiply(product))