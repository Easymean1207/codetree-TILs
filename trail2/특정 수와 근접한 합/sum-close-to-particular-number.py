import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
minDiff = sys.maxsize # 차이값 선언

sumArr = sum(arr)

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        currentSum = sumArr - arr[i] - arr[j] # 현재 회차의 합(T) 계산
        currentDiff = abs(currentSum - S) # 현재 회차의 |T-S|계산

        minDiff = min(minDiff, currentDiff) # 비교후, 최소 차이값 갱신

print(minDiff)
