commands = input()

# Please write your code here.
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
#     E   S  W  N

x, y = 0, 0
direction = 3 # 처음 방향은 N(북쪽)
time = 0
firstComeBackTime = -1

for command in commands:
    if command == 'L':
        # 왼쪽으로 90도 회전
        direction = (direction+3)%4
    elif command == 'R':
        # 오른쪽으로 90도 회전
        direction = (direction+1)%4
    elif command == 'F':
        # 현재 방향으로 1만큼 전진
        x+= dx[direction]
        y+= dy[direction]
    else:
        pass
    
    time+=1 # 모든 명령은 1초씩 걸림

    if x == 0 and y == 0:
        firstComeBackTime = time
        break

print(firstComeBackTime)