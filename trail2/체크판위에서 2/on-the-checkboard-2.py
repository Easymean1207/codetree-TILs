R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
numberOfCase = 0
startColor = grid[0][0]
endColor = grid[R-1][C-1]

# 첫째 중간 지점
for i in range(1, R):
    for j in range(1, C):
        # 두 번째 중간 지점 
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
                # 시작 -> 첫째 중간 지점 -> 둘째 중간 지점 -> 도착
                # 이동할 때 마다 색은 항상 달라야 함
                if (startColor != grid[i][j]
                    and grid[i][j] != grid[k][l]
                    and grid[k][l] != endColor):

                    numberOfCase+=1

print(numberOfCase)
