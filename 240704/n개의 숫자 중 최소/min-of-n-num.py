n = int(input())
nums = list(map(int,input().split()))


''' for문을 이용한 방법 '''
min_value = nums[0]
cnt = 0

for i,num in enumerate(nums[1:]):
    if num < min_value:
        min_value = num

''' min() 함수를 이용한 방법 '''
# min_value = min(nums)
min_cnt = nums.count(min_value)

print(f'{min_value} {min_cnt}')