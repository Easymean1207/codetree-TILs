n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs, dys = [0,1,0,-1], [1,0,-1,0] # 우(E), 하(W), 좌(W), 상(N)
threeOrMoreCount = 0 # 인접한 칸 중 1이 적힌 칸이 3개 이상인 칸의 개수

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for x in range(n):
    for y in range(n):
        adjacentCount = 0 # 인접한 칸의 개수
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                adjacentCount += 1
        
        if adjacentCount >=3:
            threeOrMoreCount+=1

print(threeOrMoreCount)