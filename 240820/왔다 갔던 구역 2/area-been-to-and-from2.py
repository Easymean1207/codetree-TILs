# ''' 
#     위치 0에서 시작
#     n번의 명령(최대 100회)
#     x L -> 왼쪽으로 x만큼 이동
#     x R -> 오른쪽으로 x만큼 이동 
# '''
# 최대 범위, 오프셋 설정
MAX_RANGE = 2000
OFFSET = 1000

# n번의 명령
n = int(input())

# 0(1000)에서 시작
start = OFFSET

# 최대 이동 ⭐구간⭐ 설정(-1000(0) ~ 1000(2000))
location = [0 for _ in range(MAX_RANGE+1)]

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == 'R':
        for i in range(start, start+distance):
            location[i] +=1
        start += distance

    if direction == 'L':
        for i in range(start, start-distance, -1):
            location[i] +=1
        start -= distance

cnt = 0
for i in range(len(location)):
    if location[i] >=2:
        cnt += 1

print(cnt)

# segments = []
# current = 0

# for _ in range(n):
#     distance, direction = input().split()
#     distance = int(distance)

#     # 왼쪽 이동의 경우 : current - distance ~ cur의 범위 
#     if direction == 'L':
#         left_range = current - distance
#         right_range = current
#         current -= distance
    
#     # 오른쪽 이동의 경우 : current ~ current + distance의 범위
#     elif direction == 'R':
#         left_range = current
#         right_range = current + distance
#         current += distance
    
#     segments.append([left_range,right_range])

# location = [0 for _ in range(MAX_RANGE+1)]

# for x1, x2 in segments:
#     x1, x2 = x1 + OFFSET, x2 + OFFSET

#     for i in range(x1,x2):
#         location[i]+=1

# cnt = 0
# for visit in location:
# 	if visit >= 2:
# 		cnt += 1
# print(cnt)