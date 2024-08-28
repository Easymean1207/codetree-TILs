OFFSET = 100
MAX_RANGE = OFFSET*2

# 초기 좌표평면 설정
coordinate = [[0]*(MAX_RANGE+1) for _ in range(MAX_RANGE+1)]

# 직사각형 개수 n
n = int(input())

for i in range(1, n+1):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    # 오프셋 적용
    x1, y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            # 홀수 번째의 경우 -> 빨간색(1)
            if i %2 == 1:
                coordinate[x][y] = 1
            # 짝수 번째의 경우 -> 파란색(-1)
            else:
                coordinate[x][y] = -1
    
    area = sum(coordinate[x][y] == -1 for x in range(MAX_RANGE+1) for y in range(MAX_RANGE+1))

print(area)