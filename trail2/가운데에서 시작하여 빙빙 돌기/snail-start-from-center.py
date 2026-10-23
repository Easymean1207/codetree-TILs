n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.

# 안이 아닌 밖에서부터 채워나가는 방식으로 접근

# 0: 왼쪽, 1:위쪽 2:오른쪽 3:아래쪽
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

r, c = n-1, n-1 # (n-1, n-1)에서 시작
direction = 0 # 처음 시작 방향은 왼쪽

def in_range(r, c):
    return (r>=0 and r<n) and (c>=0 and c<n)

for num in range(n*n, 0, -1):
    grid[r][c] = num # 해당 칸에 숫자 채우기

    # 현재 위치에서 지정된 방향으로 1칸 이동
    nr = r + dr[direction]
    nc = c + dc[direction]

    # 이동한 위치가 범위를 벗어나거나 이미 값이 채워져있다면 회전
    if not in_range(nr,nc) or grid[nr][nc] !=0:
        direction = (direction+1)%4
    
    r += dr[direction]
    c += dc[direction]
    
for row in grid:
    for element in row:
        print(element, end = ' ')
    print()


