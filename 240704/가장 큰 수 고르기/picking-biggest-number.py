nums = list(map(int, input().split()))

''' for문을 이용한 기본적 방법 '''
# max_value = nums[0]

# for num in nums[1:]:
#     if num > max_value:
#         max_value = num

''' python의 max() 함수를 이용한 방법 '''
print(max(nums))