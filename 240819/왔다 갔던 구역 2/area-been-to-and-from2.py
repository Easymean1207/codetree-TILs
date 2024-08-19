''' 
    위치 0에서 시작
    n번의 명령(최대 100회)
    x L -> 왼쪽으로 x만큼 이동
    x R -> 오른쪽으로 x만큼 이동 
'''
# 최대 범위, 오프셋 설정
MAX_RANGE = 2000
OFFSET = 1000

# n번의 명령
n = int(input())

# 0(1000)에서 시작
start = OFFSET

# 최대 이동 구간 설정(-1000(0) ~ 999(1999))
location = [0 for _ in range(MAX_RANGE)]

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)


    if direction == 'R':
        for i in range(distance):
            location[start+i] +=1
        start += distance

    if direction == 'L':
        for i in range(1,distance+1):
            location[start-i] +=1
        start -= distance

cnt = 0
for i in range(len(location)):
    if location[i] >=2:
        cnt += 1

print(cnt)