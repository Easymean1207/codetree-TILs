N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

A_movements = [0] * (sum(t) + 1) # A가 이동한 거리
B_movements = [0] * (sum(t2) + 1) # B가 이동한 거리

# Please write your code here.
currentTimeA = 1 # A의 현재 시간
currentTimeB = 1 # B의 현재 시간

# 각 구간의 속도로, 그 구간의 시간만큼 1초씩 위치를 기록
for i in range(N):
    for _ in range(t[i]):
        A_movements[currentTimeA] = A_movements[currentTimeA-1] + v[i]
        currentTimeA+=1
# print(A_movements)

for i in range(M):
    for _ in range(t2[i]):
        B_movements[currentTimeB] = B_movements[currentTimeB-1] + v2[i]
        currentTimeB+=1
# print(B_movements)

minTime = min(len(A_movements), len(B_movements)) # 둘 중 최소 시간
changedCount = 0; # 선두가 바뀐 횟수
prevLeader = ''; # 이전 선두

# 선두가 바뀐 횟수 계산
for i in range(1, minTime):
    if A_movements[i] > B_movements[i]:
        currentLeader = 'A'
    elif A_movements[i] < B_movements[i]:
        currentLeader = 'B'
    else:
        currentLeader = 'AB'

    # 선두가 바뀌면 선두를 교체하고 changedCount를 1 증가
    if prevLeader != currentLeader:
        prevLeader = currentLeader
        changedCount +=1

print(changedCount)