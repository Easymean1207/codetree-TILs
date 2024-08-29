# n개의 숫자
N = int(input())

nums = []
result = 0
same_sign_cnt = 0

for i in range(N):
    num = int(input())
    nums.append(num)

for i in range(len(nums)):
    # 연속하는 숫자의 부호가 같은 경우 -> same_sign_cnt를 1 증가
    if i == 0 or (nums[i] * nums[i-1] > 0):
        same_sign_cnt+=1
    # 연속하는 숫자의 부호가 다른 경우 -> same_sign_cnt를 1로 초기화
    else:
        result = max(same_sign_cnt, result)
        same_sign_cnt = 1
    
result = max(same_sign_cnt, result)
print(result)