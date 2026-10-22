n, m = map(int, input().split())

# Please write your code here.
square = [[0] * m for _ in range(n)] # N행, M열 직사각형 설정

# 0:오른쪽, 1:아래쪽, 2:왼쪽, 3:위쪽
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r, c = 0, 0
direction = 0

def in_range(r, c):
    return (r>=0 and r<n) and (c>=0 and c<m)

for num in range(1, n*m+1):
    square[r][c] = num # 현재 칸에 숫자 기록

    # 현재 위치에서 지정된 방향으로 1칸 이동
    nr = r + dr[direction]
    nc = c + dc[direction]

    # 이동한 위치가 범위를 벗어나거나 이미 값이 채워져있다면 회전
    if not in_range(nr,nc) or square[nr][nc] != 0:
        direction = (direction + 1) % 4
    
    # 현재 위치를 이동한 위치로 갱신
    r = r + dr[direction]
    c = c + dc[direction]

for row in square:
    for element in row:
        # 직사각형의 숫자를 알파벳으로 변경
        alphabet = chr(65 + (element-1) % 26)
        print(alphabet, end = ' ')
    print()
