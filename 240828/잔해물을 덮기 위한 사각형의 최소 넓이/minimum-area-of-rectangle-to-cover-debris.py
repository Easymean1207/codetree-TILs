'''
    첫 번째 직사각형 좌측 하단 좌표(x1, y1), 우측 상단 좌표(x2, y2)
    두 번째 칙사각형 좌측 하든 좌표(x3, y3), 우측 상단 좌표(x4, y4)
'''

OFFSET = 1000
MAX_RANGE = OFFSET *2

# 첫 번째 직사각형 좌표
x1, y1, x2, y2 = tuple(map(int, input().split()))
# 두 번째 직사각형 좌표
x3, y3, x4, y4 = tuple(map(int, input().split()))

# 오프셋 적용
x1, y1, x2, y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
x3, y3, x4, y4 = x3+OFFSET, y3+OFFSET, x4+OFFSET, y4+OFFSET

# 좌표 설정
coordinate = [
    [0 for _ in range(MAX_RANGE+1)]
    for _ in range(MAX_RANGE + 1)
]

# 첫 번째 직사각형 표시
for i in range(x1, x2):
    for j in range(y1, y2):
        coordinate[i][j] = 1

# 두 번째 직사각형 표시
for i in range(x3, x4):
    for j in range(y3, y4):
        coordinate[i][j] = 2

# 겹치는 지 판별을 위한 변수
isOverlapped = False
remained_x1, remained_y1, remained_x2, remained_y2 = MAX_RANGE, MAX_RANGE, 0, 0

# 겹치지 않는 부분 (아직 1로 남아있는 부분) 표시
for i in range(MAX_RANGE+1):
    for j in range(MAX_RANGE+1):
        if coordinate[i][j] == 1:
            isOverlapped = True
            remained_x1 = min(remained_x1, i)
            remained_y1 = min(remained_y1, j)
            remained_x2 = max(remained_x2, i)
            remained_y2 = max(remained_y2, j)

# print(remained_x1, remained_y1, remained_x2, remained_y2)

if not isOverlapped:
    remain_area = 0
else:
    remain_area = (remained_x2+1 - remained_x1) * (remained_y2+1 - remained_y1)

print(remain_area)