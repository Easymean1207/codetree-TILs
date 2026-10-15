n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
currentX = 0
currentY = 0

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # N, S, E, W

for direction, distance in moves:
    distance = int(distance)

    if direction == 'N':
        currentX += dx[0] * distance
        currentY += + dy[0] * distance
    elif direction == 'S':
        currentX += dx[1] * distance
        currentY += dy[1] * distance
    elif direction == 'E':
        currentX += dx[2] * distance
        currentY += dy[2] * distance
    elif direction == 'W':
        currentX += dx[3] * distance
        currentY += dy[3] * distance
    else:
        continue

print(currentX, currentY)