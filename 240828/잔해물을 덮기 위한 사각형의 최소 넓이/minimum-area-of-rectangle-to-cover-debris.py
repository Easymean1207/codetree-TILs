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

# 첫 번째 직사각형의 넓이
rect1 = (x2 - x1) * (y2 - y1)

# 겹치는 영역의 좌표
overlap_x1 = max(x1, x3)
overlap_y1 = max(y1, y3)
overlap_x2 = min(x2, x4)
overlap_y2 = min(y2, y4)

# 겹치는 영역 구하기
if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
    overlap_area = (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)
else:
    overlap_area = 0

extra_need = rect1
print(extra_need)