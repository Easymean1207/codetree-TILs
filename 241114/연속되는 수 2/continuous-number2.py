# 숫자의 개수(N)
N = int(input())

cnt = 0
result = 0

nums = [
    int(input())
    for _ in range(N)
]

for i in range(N):
    # 연속해서 같은 숫자가 나오는 경우 -> cnt 증가
    if nums[i-1] == nums[i]: 
        cnt +=1
    
    # 다음 숫자가 다른 경우 -> result 갱신, cnt를 1로 초기화
    else:
        result = max(result, cnt)
        cnt = 1

print(result)