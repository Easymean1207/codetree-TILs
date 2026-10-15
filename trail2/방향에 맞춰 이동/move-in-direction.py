n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
currentX = 0
currentY = 0

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # N, S, E, W

for i in range(n):
    if dir[i] == 'N':
        currentX += dx[0] * dist[i]
        currentY += dy[0] * dist[i]
    elif dir[i] == 'S':
        currentX += dx[1] * dist[i]
        currentY += dy[1] * dist[i]
    elif dir[i] == 'E':
        currentX += dx[2] * dist[i]
        currentY += dy[2] * dist[i]
    elif dir[i] == 'W':
        currentX += dx[3] * dist[i]
        currentY += dy[3] * dist[i]
    else:
        continue

print(currentX, currentY)
