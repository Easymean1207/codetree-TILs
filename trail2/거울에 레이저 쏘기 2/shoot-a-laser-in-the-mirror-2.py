n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
def in_range(r, c):
    return (r>=0 and r<n) and (c>=0 and c<n)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
#    위  오  아  왼

# '/' 거울에서의 방향 변화
slash = [1, 0, 3, 2]
# '\' 거울에서의 방향 변화
backslash = [3, 2, 1, 0]

reflectedCount = 0 # 튕긴 횟수 설정

# k가 어느 변에 위치하는지 계산
# 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽
side = (k-1)//n

# K의 위치에 따라 시작 좌표 계산
if side == 0:  # K가 윗변에 위치
    r = 0
    c = k - 1
elif side == 1:  # K가 오른변에 위치
    r = k - n - 1
    c = n - 1
elif side == 2:  # K가 아랫변에 위치
    r = n - 1
    c = 3 * n - k
elif side == 3:  # K가 왼쪽변에 위치
    r = 4 * n - k
    c = 0

direction = (side + 2) % 4 # 방향 설정(위(아래) -> 아래(위), 왼쪽(오른쪽) -> 오른쪽(왼쪽))

while in_range(r,c):
    # 거울에 따라 방향 변경
    if grid[r][c] == '/':
        direction = slash[direction]

    elif grid[r][c] == '\\':
        direction = backslash[direction]
    
    reflectedCount+=1 # 튕긴 횟수 1증가

    r = r + dr[direction]
    c = c + dc[direction]

print(reflectedCount)