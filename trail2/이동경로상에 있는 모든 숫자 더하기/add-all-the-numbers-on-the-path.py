N, T = map(int, input().split())
commands = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

# N X N 격자, T개의 명령(L,R,F)

# 0: 동, 1: 남, 2: 서, 3: 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r, c = (N-1)//2, (N-1)//2 # 가운데에서 시작
direction = 3 # 북쪽을 바라본 상태에서 시작
total = board[r][c] # 최초 총합은 가운데 값

def in_range(r, c):
    return (r>=0 and r<N) and (c>=0 and c<N)


for command in commands:
    # 왼쪽 회전
    if command == 'L':
        direction = (direction + 3) % 4
    # 오른쪽 회전
    elif command == 'R':
        direction = (direction + 1) % 4
    # 전진
    elif command == 'F':
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 격자를 벗어나지 않는다면 해당 칸의 값을 총합에 더하기
        if in_range(nr, nc):
            r, c = nr, nc
            total += board[r][c]
    
print(total)
