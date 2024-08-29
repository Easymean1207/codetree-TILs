# 숫자의 개수 N
N = int(input())

same_cnt = 0
result = 0
nums = []

for i in range(N):
    num = int(input())
    nums.append(num)

# print(nums)

for i in range(N):
    # 연속해서 같은 숫자가 나오는 경우 -> same_cnt를 1 증가
    if nums[i] == nums[i-1]:
        same_cnt+=1
    # 연속이 끊기는 경우 -> result 재설정, same_cnt를 1로 초기화
    else:
        result = max(result, same_cnt)
        same_cnt = 1

print(result)