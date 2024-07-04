n = int(input())
nums = list(map(int, input().split()))

cnt = 0
third_idx = 0

for i, num in enumerate(nums):
    if num == 2:
        cnt+=1
        if cnt == 3:
            third_idx = i+1

print(third_idx)