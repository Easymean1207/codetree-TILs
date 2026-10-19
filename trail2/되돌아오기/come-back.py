N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
#     E   S  W  N

mappedDirection = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

x, y = 0, 0
time = 0
firstComeBackTime = -1

for i in range(N):
    for _ in range(dist[i]): # dist[i](i번째 거리만큼 반복)
        # i번째 방향을 mappedDirection에서 찾아서 매핑
        direction = mappedDirection[dir[i]]

        x = x + dx[direction]
        y = y + dy[direction]

        time+=1

        # 처음으로 돌아오면 firstComeBackTime 갱신
        if x == 0 and y == 0:
            firstComeBackTime = time
    
    # firstComeBackTime이 갱신되었을 때 바깥 루프도 탈출
    if firstComeBackTime != -1:
        break 

print(firstComeBackTime)  