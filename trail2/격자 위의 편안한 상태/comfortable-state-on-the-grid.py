n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def in_range(r, c):
    return (r>=0 and r<n) and (c>=0 and c<n)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
#     우  하  좌  상

grid = [[0] * n for _ in range(n)] # 색을 칠할 격자 설정

for r,c in points:
    # 배열은 0부터 시작
    r -=1
    c -=1

    # 해당 칸에 색칠을 칠하고 색칠된 인접칸 개수를 0으로 설정
    grid[r][c]=1
    adjacentColoredCount=0

    for each_direction in range(4):
        # 해당 칸의 인접 칸들(상하좌우)
        nr = r + dr[each_direction]
        nc = c + dc[each_direction]

        # 인접 칸이 격자 내의 유효한 범위이고 색칠되어있다면
        if in_range(nr, nc) and grid[nr][nc] == 1:
            adjacentColoredCount+=1 # adjacentColoredCount 1 증가
    
    if adjacentColoredCount == 3:
        print(1)
    else:
        print(0)


