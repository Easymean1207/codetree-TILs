import sys

nums = list(map(int, input().split()))

min_value = sys.maxsize
max_value = -sys.maxsize

for num in nums:
    if num == 999 or num == -999:
        break
    
    if num < min_value:
        min_value = num
    
    if num > max_value:
        max_value = num

print(f'{max_value} {min_value}')