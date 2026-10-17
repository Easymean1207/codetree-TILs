n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

def in_range(r,c):
    return r >= 0 and r < n and c >= 0 and c < m

def shouldRotate(r, c):
    return not in_range(r, c) or arr[r][c] != 0

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 0; # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
current_r, current_c = 0, 0

arr[current_r][current_c] = 1 # 초기 시작은 1부터

for i in range(2, n*m+1):
    nr, nc = current_r + dr[direction], current_c + dc[direction] # 위치값 계산

    # 격자의 끝에 도달했거나 이미 값이 존재한다면 시계방향으로 회전
    if shouldRotate(nr, nc):
        direction = (direction + 1) % 4
    
    # 회전한 뒤에 이동하고 값을 채움
    current_r, current_c = current_r + dr[direction], current_c + dc[direction]
    arr[current_r][current_c] = i

for row in arr:
    for element in row:
        print(element, end = ' ')
    print()
