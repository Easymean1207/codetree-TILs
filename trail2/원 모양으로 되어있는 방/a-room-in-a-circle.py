import sys
INT_MAX = sys.maxsize

n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
minTotalDistance = INT_MAX

for startRoom in range(n):
    totalDistance = 0

    # 시작 방에서 각 방까지의 거리 계산
    for i in range(n):
        distance = (i - startRoom + n) % n
        totalDistance += distance * a[i]
    
    minTotalDistance = min(minTotalDistance, totalDistance)

print(minTotalDistance)