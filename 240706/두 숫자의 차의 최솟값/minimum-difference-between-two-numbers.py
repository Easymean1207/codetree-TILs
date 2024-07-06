n = int(input())

nums = list(map(int, input().split()))

min_differ = nums[0]

# 입력값들이 오름차순이기에 차이의 최소는 반드시 인접한 값에서만 발생
for i in range(1,len(nums)):
    differ = nums[i] - nums[i-1]

    if differ < min_differ:
        min_differ = differ

print(min_differ)