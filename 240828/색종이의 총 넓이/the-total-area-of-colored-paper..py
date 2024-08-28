'''
    8 x 8 색종이 n장
    (-100, -100) ~ (100, 100)
    겹치는 영역은 단 한번만 넓이에 포함
'''
OFFSET = 100
MAX_R = 100 * 2
coordinate = [
    [0 for _ in range(MAX_R+1)]
    for _ in range(MAX_R+1)
]

# 색종이 개수 N
N = int(input())

for _ in range(N):
    # 좌하단 좌표
    x, y = tuple(map(int, input().split()))
    x, y = x + OFFSET, y + OFFSET
    
    # 색종이 표시
    for i in range(x, x+8):
        for j in range(y, y+8):
            coordinate[i][j] = 1
    
    # 영역 선언
    area_width = 0

    # 좌표에 사각형의 영역 추가
    for i in range(MAX_R+1):
        for j in range(MAX_R+1):
            if coordinate[i][j] == 1:
                area_width +=1

print(area_width)