import sys

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
INT_MAX = sys.maxsize
minTotalDistance = INT_MAX

for gatherHouse in range(n):
    totalDistance = 0

    for currentHouse in range(n):
        distance = abs(currentHouse - gatherHouse) # 거리는 (모일 집 - 현재 집)

        totalDistance = totalDistance + distance * A[currentHouse]
    
    minTotalDistance = min(minTotalDistance, totalDistance)

print(minTotalDistance)



