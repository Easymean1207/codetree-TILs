n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
def in_range(r, c):
    return (r>=0 and r<n) and (c>=0 and c<n)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
#    위  오  아  왼

reflectedCount = 0 # 튕긴 횟수 설정

# K의 위치와 진행방향 설정
if k >= 1 and k <= n: # K가 윗변에 위치, 아래쪽으로 진행
    r = 0
    c = k-1
    direction = 2
elif k >= n+1 and k <= 2*n: # K가 오른변에 위치, 왼쪽으로 진행
    r = k-1-n
    c = n-1
    direction = 3
elif k >= 2*n+1 and k <= 3*n: # K가 아래변에 위치, 위쪽으로 진행
    r = n-1
    c = 3*n-k
    direction = 0
elif k >= 3*n+1 and k <= 4*n: # K가 왼쪽변에 위치, 오른쪽으로 진행
    r = 4*n-k
    c = 0
    direction = 1

while in_range(r,c):
    # 거울에 따라 방향 변경
    if grid[r][c] == '/':
        if direction == 0: # 위쪽 -> 오른쪽
            direction = 1
        elif direction == 1: # 오른쪽 -> 위쪽
            direction = 0
        elif direction == 2: # 아래쪽 -> 왼쪽
            direction = 3
        elif direction == 3: # 왼쪽 -> 아래쪽
            direction = 2

    elif grid[r][c] == '\\':
        if direction == 0: # 위쪽 -> 왼쪽
            direction = 3
        elif direction == 1: # 오른쪽 -> 아래쪽
            direction = 2
        elif direction == 2: # 아래쪽 -> 오른쪽
            direction = 1
        elif direction == 3: # 왼쪽 -> 위쪽
            direction = 0
    
    reflectedCount+=1 # 튕긴 횟수 1증가

    r = r + dr[direction]
    c = c + dc[direction]

print(reflectedCount)