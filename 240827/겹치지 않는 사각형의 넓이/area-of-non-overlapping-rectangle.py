# OFFSET, 최대 범위 지정
OFFSET = 1000
MAX_RANGE = OFFSET * 2

# 최대 범위를 포함하는 2차원 배열(직사각형)
grid = [[0]*(MAX_RANGE+1) for _ in range(MAX_RANGE+1)]

# 직사각형 A의 좌표 (x1, y1, x4, y2)
x1, y1, x2, y2 = tuple(map(int, input().split()))
# 직사각형 B의 좌표 (x3, y3, x4, y4)
x3, y3, x4, y4 = tuple(map(int, input().split()))
# 직사각형 M의 좌표 (x5, y5, x6, y6)
x5, y5, x6, y6 = tuple(map(int, input().split()))

# OFFSET 적용
x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
x3, y3, x4, y4 = x3 + OFFSET, y3 + OFFSET, x4 + OFFSET, y4 + OFFSET
x5, y5, x6, y6 = x5 + OFFSET, y5 + OFFSET, x6 + OFFSET, y6 + OFFSET

''' '''
# 직사각형 A의 넓이 적용(각 sector당 1로 설정)
for i in range(x1, x2):
    for j in range(y1, y2):
        grid[i][j] = 1

# 직사각형 B의 넓이 적용(각 sector당 1로 설정)
for i in range(x3, x4):
    for j in range(y3, y4):
        grid[i][j] = 1

# 직사각형 M의 넓이 적용(각 sector당 -1로 설정)
for i in range(x5, x6):
    for j in range(y5, y6):
        grid[i][j] = -1

area_width = 0

for i in range(MAX_RANGE+1):
    for j in range(MAX_RANGE+1):
        if grid[i][j] == 1:
            area_width+=1

print(area_width)