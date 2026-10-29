n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]


# Please write your code here.
totalDistance = 0
maxSavedDistance = 0

for i in range(1, len(points)):
    totalDistance = totalDistance + abs(x[i-1] - x[i]) + abs(y[i-1] - y[i])

for i in range(1, n-1):
    # i-1 -> i -> i+1 거리
    originDistance = abs(x[i]-x[i-1]) + abs(y[i]-y[i-1]) + abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
    # i-1 -> i+1 거리
    bypassDistance = abs(x[i+1] - x[i-1]) + abs(y[i+1] - y[i-1])

    # 건너뛰었을 때 절약 가능한 거리 계산
    savedDistance = originDistance - bypassDistance
    # 현재 savedDistance와 이전 max값을 비교해서 큰 쪽을 저장
    maxSavedDistance = max(maxSavedDistance, savedDistance)

print(totalDistance - maxSavedDistance)

