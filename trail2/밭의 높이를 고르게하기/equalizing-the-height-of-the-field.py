# N개의 밭 (1 <= N <= 100)
# T번 이상 (1 <= T <= 10)
# H 높이 (1 <= H <= 100)
N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys


minCost = sys.maxsize

for i in range(N-T+1): # 시작점
    cost = 0
    # i ~ T 구간 별로 비용 계산
    for j in range(i, i+T):
        cost += abs(arr[j] - H)
    
    # 최솟값
    minCost = min(minCost, cost)

print(minCost)
