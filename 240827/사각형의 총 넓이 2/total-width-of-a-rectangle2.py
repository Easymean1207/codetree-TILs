OFFSET = 100
MAX_RANGE = 2 * OFFSET

# 직사각형의 개수 N
N = int(input())

# 최대 200 x 200의 넓이를 가지는 사각형 생성
grid = [[0]*(MAX_RANGE+1) for _ in range(MAX_RANGE+1)]

for i in range(N):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1, x2, y2 = x1 + OFFSET , y1 + OFFSET, x2 + OFFSET , y2 + OFFSET

    for width in range(x1, x2):
        for length in range(y1, y2):
            grid[width][length] = 1

area = 0

for i in range(MAX_RANGE+1):
    for j in range(MAX_RANGE+1):
        if grid[i][j] == 1:
            area+=1

print(area)