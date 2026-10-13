n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# N개의 명령 
# 각 명령 이후에는 마지막으로 뒤집은 타일에 위치함
# 오른쪽 이동 -> 검은색으로 뒤집음
# 왼쪽 이동 -> 흰색으로 뒤집음
# x L -> 현재 위치 포함 x칸 타일을 뒤집으며 왼쪽으로 이동
# x R -> 현재 위치 포함 x칸 타일을 뒤집으며 오른쪽으로 이동
# 흰색, 타일 순서로 출력

tiles = [0] * (n * 100)
currentLocation = 0;

# 타일 뒤집기
for i in range(n):
    if(dir[i] == 'R'):
        for j in range(currentLocation, currentLocation + x[i]):
            tiles[j] = 1 # 검은색은 1로 지정
        currentLocation +=x[i] -1

    elif(dir[i] == 'L'):
        for j in range(currentLocation, currentLocation - x[i], -1):
            tiles[j] = -1 # 흰색은 -1로 지정
        currentLocation -=x[i] -1

white = tiles.count(-1)
black = tiles.count(1)

print(white, black)
