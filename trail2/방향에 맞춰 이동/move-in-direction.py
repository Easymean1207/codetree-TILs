n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
currentX = 0
currentY = 0

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # N, S, E, W

for i in range(n):
    for j in range(dist[i]):
        if dir[i] == 'N':
            currentX, currentY = currentX + dx[0], currentY + dy[0]
        elif dir[i] == 'S':
            currentX, currentY = currentX + dx[1], currentY + dy[1]
        elif dir[i] == 'E':
            currentX, currentY = currentX + dx[2], currentY + dy[2]
        elif dir[i] == 'W':
            currentX, currentY = currentX + dx[3], currentY + dy[3]
        else:
            continue
print(currentX, currentY)
    


