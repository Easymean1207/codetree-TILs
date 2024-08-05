def groupingAndFind(nums):
    sorted_nums = sorted(nums)
    # print(sorted_nums)
    biggest = 0
    # print(biggest)

    for i in range(int(len(sorted_nums)/2)):
        candidate = sorted_nums[i] + sorted_nums[-(i+1)]
        biggest = max(biggest, candidate)
        
    return biggest


group_nums = int(input())
nums = list(map(int,input().split()))

result = groupingAndFind(nums)
print(result)