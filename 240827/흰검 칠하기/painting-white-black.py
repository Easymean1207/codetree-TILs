''' 
    아무 타일에서 시작
    n번의 명령
    x L -> 왼쪽으로 이동, 현재 타일 포함 흰색으로
    x R -> 오른쪽으로 이동, 현재 타일 포함 검은색으로
    각 명령 후 마지막 타일에 위치
    타일이 각각 검은색, 흰색이 2번 되면 회색이 됨
'''
OFFSET = 100
MAX_RANGE = 1000 * OFFSET * 2

# n번의 명령
n = int(input())

# 명령을 담을 리스트
commands = []

# 흰색, 검은색 색칠 기록을 위한 배열
white_record = [0] * (2 * MAX_RANGE + 1)
black_record = [0] * (2 * MAX_RANGE + 1)
# 실제 검,흰,회 개수
black_cnt, white_cnt, gray_cnt = 0, 0 , 0

start = 0

# 각 명령 세분화
for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == 'L':
        left_range = start - distance
        right_range = start
        start-=distance

    elif direction == 'R':
        left_range = start
        right_range = start + distance
        start+=distance

    commands.append([left_range, right_range, direction])

# print(commands)

location = [0 for _ in range(MAX_RANGE+1)]

for x1, x2, direction in commands:
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    for i in range(x1, x2):
        # 방향이 'L'인 경우 해당 범위만큼 흰색으로 색칠
        if direction == 'L':
            location[i] = -1
            white_record[i] +=1

        # 방향이 'R'인 경우 해당 범위만큼 검은색으로 색칠
        elif direction == 'R':
            location[i] = 1
            black_record[i] +=1

for i in range(len(location)):
    # 검, 흰이 2번 이상인 경우는 회색
    if black_record[i] >=2 and white_record[i] >=2:
        gray_cnt +=1
    # 그 외의 경우는 마지막에 색칠된 색을 따라감    
    elif location[i] == -1:
        white_cnt +=1
    elif location[i] == 1:
        black_cnt +=1

print(white_cnt, black_cnt, gray_cnt)