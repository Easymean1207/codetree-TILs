n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.

# 안이 아닌 밖에서부터 채워나가는 방식으로 접근

# # 0: 왼쪽, 1:위쪽 2:오른쪽 3:아래쪽
# dr = [0, -1, 0, 1]
# dc = [-1, 0, 1, 0]

# r, c = n-1, n-1 # (n-1, n-1)에서 시작
# direction = 0 # 처음 시작 방향은 왼쪽

# def in_range(r, c):
#     return (r>=0 and r<n) and (c>=0 and c<n)

# for num in range(n*n, 0, -1):
#     grid[r][c] = num # 해당 칸에 숫자 채우기

#     # 현재 위치에서 지정된 방향으로 1칸 이동
#     nr = r + dr[direction]
#     nc = c + dc[direction]

#     # 이동한 위치가 범위를 벗어나거나 이미 값이 채워져있다면 회전
#     if not in_range(nr,nc) or grid[nr][nc] !=0:
#         direction = (direction+1)%4
    
#     r += dr[direction]
#     c += dc[direction]
    
# for row in grid:
#     for element in row:
#         print(element, end = ' ')
#     print()


# 2. 안쪽에서 접근해서 바깥으로 나가는 방법

# 0: 오른쪽, 1: 위쪽, 2: 왼쪽, 3: 아래쪽
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

r, c = (n - 1) // 2, (n - 1) // 2 # 정가운데에서 시작

direction = 0 # 처음 방향은 오른쪽

requireMoveCount = 1 # 이번 방향으로 몇 칸 이동해야 하는지
currentMoveCount = 0 # 이번 방향으로 지금까지 몇 칸 이동했는지
turnCount = 0 # 같은 목표 거리로 몇 번 이동했는지

for num in range(1, n*n+1):
    grid[r][c] = num

    # 현재 방향으로 1칸 이동
    r += dr[direction]
    c += dc[direction]

    currentMoveCount+=1 # 이동 거리 1 증가

    # 목표 거리만큼 이동했다면 회전
    if currentMoveCount == requireMoveCount:
        direction = (direction + 1) % 4
        currentMoveCount = 0 # 이동 거리 초기화
        turnCount +=1 # 회전 횟수 1 증가

        # 같은 목표 거리를 2번 이동했다면
        if turnCount == 2:
            requireMoveCount +=1 # 목표 거리를 1 증가
            turnCount = 0 # 회전 횟수 초기화

for row in grid:
    for element in row:
        print(element, end = ' ')
    print()