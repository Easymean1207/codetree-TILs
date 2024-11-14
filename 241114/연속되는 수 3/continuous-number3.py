# N개의 숫자
N = int(input())

nums = [
    int(input())
    for _ in range(N)
]

result = 0
same_sign_cnt = 0

for i in range(len(nums)):
    # 연속하는 숫자의 부호가 같은 경우 -> same_sign_cnt 1 증가
    if i == 0 or (nums[i-1] * nums[i]) > 0:
        same_sign_cnt +=1
    else:
        same_sign_cnt = 1
    
    result = max(same_sign_cnt, result)

print(result)