dirs = input()

# Please write your code here.
x, y = 0, 0 # 초기 위치
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # E, S, W, N

viewDirection = 3 # 처음에는 북쪽을 향하고 있음

for dir in dirs:
    if dir == 'L': # 반시계
        viewDirection = (viewDirection + 3) %4
    elif dir == 'R':
        viewDirection = (viewDirection + 1) %4
    elif dir == 'F':
        x, y = x + dx[viewDirection], y + dy[viewDirection]
    else:
        continue

print(x, y)
