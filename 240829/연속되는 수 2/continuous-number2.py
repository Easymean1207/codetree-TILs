# 숫자의 개수 N
N = int(input())

same_cnt = 0
result = 0
nums = []

for i in range(N):
    num = int(input())
    nums.append(num)

for i in range(N):
    # 연속해서 같은 숫자가 나오는 경우 -> same_cnt를 1 증가
    if i == 0 or nums[i] == nums[i-1]:
        same_cnt+=1
    # 연속이 끊기는 경우 -> same_cnt를 1로 초기화
    else:
        same_cnt = 1

result = max(result, same_cnt)
print(result)